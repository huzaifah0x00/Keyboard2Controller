import ctypes
import struct, time
import numpy as np
CONST_DLL_VJOY = "vJoyInterface.dll"
global joystickPosition
joystickPosition = ""
class vJoy(object):
	def __init__(self,reference):
		self.handle = None
		self.dll = ctypes.CDLL( CONST_DLL_VJOY )
		print(dir(self.dll))
		self.reference = reference
		self.acquired = False
		print(reference)
		
	def open(self):
		if self.dll.AcquireVJD( self.reference ):
			self.acquired = True
			return True
		return False
	
	def close(self):
		if self.dll.RelinquishVJD( self.reference ):
			self.acquired = False
			return True
		return False
	def JoyStickState(self):
		return self.dll.JoyStickState()
	def generateJoystickPosition(self, 
		wThrottle = 0, wRudder = 0, wAileron = 0,

		# left thb x		left thb y	 left trigger
		wAxisX = 0x4000,   wAxisY = 0x4000,   wAxisZ = 0,

		# right thb x	   right thb y		right trigger
		wAxisXRot = 0x4000, wAxisYRot = 0x4000, wAxisZRot = 0,

		# ???		 ???		???
		wSlider = 0, wDial = 0, wWheel = 0,
		# ???		 ???		???
		wAxisVX = 0, wAxisVY = 0, wAxisVZ = 0,
		# ???		 ???				???				   
		wAxisVBRX = 0, wAxisVBRY = 0, wAxisVBRZ = 0,
		# 1 = a
		# 2 = b  3 = a+b ??
		# 4 = x  5 = x+a ?? 6 = x+b
		# 8 = y
		lButtons = 0, bHats = 0, bHatsEx1 = 0, bHatsEx2 = 0, bHatsEx3 = 0):
		joyPosFormat = "BlllllllllllllllllllIIII"
		pos = struct.pack( joyPosFormat, self.reference, wThrottle, wRudder,
								   wAileron, wAxisX, wAxisY, wAxisZ, wAxisXRot, wAxisYRot,
								   wAxisZRot, wSlider, wDial, wWheel, wAxisVX, wAxisVY, wAxisVZ,
								   wAxisVBRX, wAxisVBRY, wAxisVBRZ, lButtons, bHats, bHatsEx1, bHatsEx2, bHatsEx3 )
		return pos
	def update(self, joystickPosition):
		if self.dll.UpdateVJD( self.reference, joystickPosition ):
			return True
		return False
	
	#Not working, send buttons one by one
	def sendButtons( self, bState ):
		joyPosition = self.generateJoystickPosition( lButtons = bState )
		return self.update( joyPosition )
	
	def setButton( self, index, state ):
		if self.dll.SetBtn( state, self.reference, index ):
			return True
		return False
def ultimate_release():
	vj.open()
	joystickPosition = vj.generateJoystickPosition()
	vj.update(joystickPosition)
	time.sleep(0.001)
	vj.close()
	return joystickPosition

def movement(keystates,wAxisX = 0x4000 , wAxisY = 0x4000):
	vj.open()
	print("vj opening")
	# wAxisY = 0x4000
	# wAxisX = 0x4000
	if keystates['UP'] and not keystates['DOWN']:   # and wAxisY != 0x1 :
		wAxisY = 0x1
	else:
		pass
		# wAxisY = 0x4000
	if keystates['DOWN'] and not keystates['UP']: # and wAxisY != 0x8000:
		wAxisY = 0x8000
	else:
		pass
		# wAxisY = 0x4000
	if keystates['LEFT'] and not keystates['RIGHT']:	# and wAxisX != 0x1:
		wAxisX = 0x1
	else:
		pass
		# wAxisX = 0x4000
	if keystates['RIGHT'] and not keystates['LEFT']:  #and wAxisX != 0x8000:
		wAxisX = 0x8000
	else:
		pass
		# wAxisX = 0x4000
	joystickPosition = vj.generateJoystickPosition(wAxisX= wAxisX , wAxisY=wAxisY)
	print(struct.unpack("BlllllllllllllllllllIIII",joystickPosition))
	vj.update(joystickPosition)
	vj.close()
	return joystickPosition
def buttons(keystates):
	if keystates['SPACE']:
		vj.SetBtn( 2 , 1)
		time.sleep(0.1)
		vj.SetBtn( 2 , 0)
	if keystates['A']:
		vj.SetBtn( 3 , 1)
		time.sleep(0.1)
		vj.SetBtn( 3 , 0)
	if keystates['S']:
		vj.SetBtn( 1 , 1)
		time.sleep(0.1)
		vj.SetBtn( 1 , 0)
	
if __name__ == '__main__':
	vj = vJoy(1)
	ultimate_release()
	for i in reversed(range(1,4)):
		print(i)
		time.sleep(1)
	print(vj.JoyStickState())