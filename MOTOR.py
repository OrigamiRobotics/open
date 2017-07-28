import CHIP_IO.SOFTPWM as SPWM
import CHIP_IO.GPIO as GPIO		##import GPIO library
from time import sleep			
GPIO.setmode(GPIO.BOARD)		##name all the pins
GPIO.setup("CSID3", GPIO.OUT)		##set pins as output
GPIO.setup("CSID5", GPIO.OUT)

##Move forward

GPIO.output("CSID5", False)
GPIO.output("CSID3", True)
SPWM.start("CSID7")
SPWM.set_duty_cycle("CSID7", 100)
SPWM.cleanup()
