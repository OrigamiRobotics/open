#import paho.mqtt.client as mqtt
#from hostdef import *
from subprocess import call
import CHIP_IO.GPIO as GPIO			##import GPIO library
GPIO.setmode(GPIO.BOARD)		##use board pin bumbering
GPIO.setup("CSID1", GPIO.OUT)	##set pin XIO-P3 to out
GPIO.outout("CSID1", True)		##Turn on GPIO pin XIO-P3


