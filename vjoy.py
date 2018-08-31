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
print("bla")
def movement(keystates):
	vj.open()
	print("vj opening")
	if keystates['UP'] and not keystates['DOWN']:
		wAxisY = 0x8000
	# else:
	# 	wAxisY = 0x4000
	elif keystates['DOWN'] and not keystates['UP']:
		wAxisY = 0x1
	else:
		wAxisY = 0x4000
	if keystates['LEFT'] and not keystates['RIGHT']:
		wAxisX = 0x1
	else:
		wAxisX = 0x4000
	if keystates['RIGHT'] and not keystates['LEFT']:
		wAxisX = 0x8000
	joystickPosition = vj.generateJoystickPosition(wAxisX= wAxisX , wAxisY=wAxisY)
	print(struct.unpack("BlllllllllllllllllllIIII",joystickPosition))
	vj.update(joystickPosition)
	vj.close()
	return joystickPosition
def ultimate_release():
	vj.open()
	joystickPosition = vj.generateJoystickPosition()
	vj.update(joystickPosition)
	time.sleep(0.001)
	vj.close()
	return joystickPosition

if __name__ == '__main__':
	vj = vJoy(1)
	ultimate_release()
	for i in reversed(range(1,4)):
		print(i)
		time.sleep(1)
	print(vj.JoyStickState())