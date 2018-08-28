import time
import  pyvjoy
j = pyvjoy.VJoyDevice(1)
j.set_button(15,1)
time.sleep(1)
j.set_button(15,0)
j.set_button(1,1)
time.sleep(1)
j.set_button(1,0)
