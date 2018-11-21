import pyvjoy 
from buttonconfig import buttonconfig

class vJoy:
	def __init__(self,joystickId):
	   self.j = pyvjoy.VJoyDevice(joystickId)
	   self.BUTTONS = {
	   # 			"Y_AXIS" : self.j.data.wAxisY,
				# "X_AXIS" : self.j.data.wAxisX,
				"Y" : 1,
				"B" : 2,
				"A" : 3,
				"X" : 4,
				"RT" : 5,
				"LT" : 6,
				"RB" : 7,
				"LB" : 8,
				"DPAD_UP" : 9,
				"DPAD_DOWN" : 10,
				"DPAD_LEFT" : 11,
				"DPAD_RIGHT" : 12,
			}
	def handle_buttons(self, keystates):
		pressedbuttons = [i for i,v in keystates.items() if v]
		unpressedbuttons = [i for i,v in keystates.items() if not v]
		for p_button in pressedbuttons:
			try:
				vj_button = self.BUTTONS[buttonconfig[p_button]]
				# print(f"PRESSING BUTTPNS {vj_button}" )
				self.j.set_button(vj_button,1)
			except KeyError:
				pass
				# print("No Config defined for this button ({})".format(p_button))

		for un_button in unpressedbuttons:
			try:
				vj_button = self.BUTTONS[buttonconfig[un_button]]
				self.j.set_button(vj_button,0)
			except KeyError:
				pass


	def handle_movement(self, keystates, wAxisX = 0x4000 , wAxisY = 0x4000):
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
