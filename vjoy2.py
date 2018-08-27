import pyvjoy 
import time
for i in reversed(range(1,4)):
	print(i)
	time.sleep(1)
j = pyvjoy.VJoyDevice(1)

time.sleep(0.5)
def B(power):
	j.set_button(2,1)
	print(power*0.005)
	time.sleep(power*0.005)
	j.set_button(2,0)
def Y():
	print(dir(j))
def Up():
	j.data.wAxisX = 0x8000
	j.update()
def Right():
	j.data.wAxisY = 0x8000
	j.update()
def Down():
	j.data.wAxisX = 0x1
	j.update()
j.reset()
j.reset_povs()
for i in range(0,200):
	Right()