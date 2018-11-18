import pyvjoy 

class vJoy:
	def __init__(self,joystickId):
	   self.j = pyvjoy.VJoyDevice(joystickId)
	def movement(self, keystates, wAxisX = 0x4000 , wAxisY = 0x4000):
		self.j.data.wAxisY = wAxisY
		self.j.data.wAxisX = wAxisX
		if keystates['UP'] and not keystates['DOWN']:   # and wAxisY != 0x1 :
			wAxisY = 0x1
			self.j.data.wAxisY = wAxisY
		else:
			pass
			# wAxisY = 0x4000
		if keystates['DOWN'] and not keystates['UP']: # and wAxisY != 0x8000:
			wAxisY = 0x8000
			self.j.data.wAxisY = wAxisY
		else:
			pass
			# wAxisY = 0x4000
		if keystates['LEFT'] and not keystates['RIGHT']:	# and wAxisX != 0x1:
			wAxisX = 0x1
			self.j.data.wAxisX = wAxisX
		else:
			pass
			# wAxisX = 0x4000
		if keystates['RIGHT'] and not keystates['LEFT']:  #and wAxisX != 0x8000:
			wAxisX = 0x8000
			self.j.data.wAxisX = wAxisX
		else:
			pass
		self.j.update()
		return self.j.data
	def buttons(self, keystates):
		if keystates['W']: 
			self.j.set_button( 1 , 1) #BUTTON Y
			# time.sleep(0.3)
		else:
			self.j.set_button( 1 , 0)
		if keystates['SPACE']: 
			print("pressing B")
			self.j.set_button( 2 , 1) #BUTTON B
			# time.sleep(0.3)
		else:
			print("Releasing B")
			self.j.set_button( 2 , 0)
		if keystates['S']: 
			self.j.set_button( 3 , 1) #BUTTON A
			# time.sleep(0.3)
		else:
			print("Releasing 3 ")
			self.j.set_button( 3 , 0)
		
		if keystates['A']: 
			self.j.set_button( 4 , 1) #BUTTON X
			# time.sleep(0.3)
		else:
			self.j.set_button( 4 , 0)
		if keystates['5']: 
			print("pressing 5")
			self.j.set_button( 5 , 1) #BUTTON
			# time.sleep(0.3)
		else:
			print("Releasing 5")
			self.j.set_button( 5 , 0)
		if keystates['LSHIFT']: 
			self.j.set_button( 6 , 1) #BUTTON RT
			# time.sleep(0.3)
		else:
			print("Releasing 6 ")
			self.j.set_button( 6 , 0)
		if keystates['R']: 
			self.j.set_button( 7 , 1) #BUTTON LB
			# time.sleep(0.3)
		else:
			self.j.set_button( 7 , 0)
		if keystates['8']: 
			self.j.set_button( 8 , 1) #BUTTON LB
			# time.sleep(0.3)
		else:
			self.j.set_button( 8 , 0)
