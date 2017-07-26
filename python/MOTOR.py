import CHIP_IO.SOFTPWM as SPWM
import CHIP_IO.GPIO as GPIO			##import GPIO library
from time import sleep			
GPIO.setmode(GPIO.BOARD)		##name all the pins
GPIO.setup("CSID3", GPIO.OUT)	##set pins as output
GPIO.setup("CSID5", GPIO.OUT)

##Move forward

GPIO.output("CSID5", False)
GPIO.output("CSID3", True)
##x=28     						##Initial suty cycle starts from 28
SPWM.start("CSID7")
SPWM.set_duty_cycle("CSID7", 100)



'''while(x<100):
	x=x+1
	SPWM.set_duty_cycle("CSID7", x)
	sleep(0.2)
	print(x)
while(x>28):
	x=x-1
	SPWM.set_duty_cycle("CSID7", x)
	sleep(0.2)
	
##Move backward
GPIO.output("CSID5", True)
GPIO.output("CSID3", False)
while(x<100):
	x=x+1
	SPWM.set_duty_cycle("CSID7", x)
	sleep(0.2)
while(x>28):
	x=x-1
	SPWM.set_duty_cycle("CSID7", x)
	sleep(0.2)
	'''
SPWM.cleanup()