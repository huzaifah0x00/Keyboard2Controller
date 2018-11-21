import pyvjoy 
from buttonconfig import buttonconfig

class vJoy:
	def __init__(self,joystickId):
		 self.j = pyvjoy.VJoyDevice(joystickId)
		 self.BUTTONS = {
				"Y" : 1,
				"B" : 2,
				"A" : 3,
				"X" : 4,
				"RT" : 5,
				"LT" : 6,
				"RB" : 7,
				"LB" : 8,
				"START" : 9,
				"SELECT" : 10,
				"LS" : 11,
				"RS" : 12,
				"DPAD_UP" :  29 ,
				"DPAD_DOWN" : 30 ,
				"DPAD_LEFT" : 31 ,
				"DPAD_RIGHT" : 32 ,

			}
	def handle_buttons(self, keystates, ):

		
		pressedbuttons = [i for i,v in keystates.items() if v]
		unpressedbuttons = [i for i,v in keystates.items() if not v]

		buttonstopress = 0 # A special variable that holds all the buttons to be pressed
		
		wAxisX = 0x4000
		wAxisY = 0x4000

		###HANDLING ALL THE BUTTONS FROM 1-32..
		
		for p_button in pressedbuttons:
			try:
				if buttonconfig[p_button] == 'Y_UP' and not buttonconfig[p_button] == 'Y_DOWN':
					wAxisY = 0x1
				if buttonconfig[p_button] == 'Y_DOWN' and not buttonconfig[p_button] == 'Y_UP':
					wAxisY = 0x8000
				if buttonconfig[p_button] == 'Y_LEFT' and not buttonconfig[p_button] == 'Y_RIGHT':
					wAxisX = 0x1
				if buttonconfig[p_button] == 'Y_RIGHT' and not buttonconfig[p_button] == 'Y_LEFT':
					wAxisX = 0x8000
				vj_button = self.BUTTONS[buttonconfig[p_button]]
				# print(f"PRESSING BUTTPNS {vj_button}" )
				# self.j.set_button(vj_button,1)
				buttonstopress += 2**(vj_button-1)


		### NOT SURE IF THERE"S A BETTER WAY TO DO THE FOLLOWING...

			except KeyError:
				pass
				# print("No Config defined for this button ({})".format(p_button))
		self.j.data.wAxisY = wAxisY
		self.j.data.wAxisX = wAxisX
		self.j.data.lButtons = buttonstopress
		self.j.update() 

