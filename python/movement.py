import paho.mqtt.client as mqtt
from hostdef import *
from subprocess import call
import CHIP_IO.SOFTPWM as SPWM
import CHIP_IO.GPIO as GPIO

#GPIO.toggle_debug()
#SPWM.toggle_debug()

# Defining PocketCHIP IO pins
left = "XIO-P6"
right = "XIO-P7"
en_l_fw = "LCD-D3"
en_l_bw = "LCD-D4"
en_r_fw = "LCD-D5"
en_r_bw = "LCD-D6"

# # Initializing IO pins
SPWM.start(left, 0)
SPWM.start(right, 0)
GPIO.setup(en_l_fw, GPIO.OUT)
GPIO.setup(en_l_bw, GPIO.OUT)
GPIO.setup(en_r_fw, GPIO.OUT)
GPIO.setup(en_r_bw, GPIO.OUT)

# #Used for calculating 
L_mag = 0
R_mag = 0


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("romibo/#",0)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg_raw):
    msg = msg_raw.payload.rstrip('\t\r\n\0').split('||')                                        #Split rate data and speech data
    #print(msg_raw.topic+" "+msg[0]+" "+msg[1])                                                 #Debug
    #Converting data into integers from -100 to 100
    if msg[0] == "disconnect":                                                                  # Debug
        client.disconnect()
    elif msg_raw.topic == "romibo/emotion":
        file = open("emotion.txt","w")
        file.write(msg[0])
        file.close()
        print("emotion received")
    elif msg_raw.topic == "romibo/action":
        x = int(float(msg[0])*100)
        y = int(float(msg[1])*100)
        L_mag = int(L_mag_calculation(x,y))
        R_mag = int(R_mag_calculation(x,y))
        print("L: "+str(L_mag)+"||R:"+str(R_mag))
        
        #left motor
        if L_mag>0:
            #set to forward
            GPIO.output(en_l_fw, 1)
            GPIO.output(en_l_bw, 0)
        elif L_mag<=0:
            #set to backward
            GPIO.output(en_l_fw, 0)
            GPIO.output(en_l_bw, 1)

            
        #set velocity via duty cycle
        SPWM.set_duty_cycle(left, abs(L_mag))

        #right motor
        if R_mag>0:
            #set to forward
            GPIO.output(en_r_fw, 1)
            GPIO.output(en_r_bw, 0)
        elif R_mag<=0:
            #set to backward
            GPIO.output(en_r_fw, 0)
            GPIO.output(en_r_bw, 1)

        #set velocity via duty cycle
        SPWM.set_duty_cycle(right, abs(R_mag))

def L_mag_calculation(x, y):
    #y indicates amount of forward movement from -100 to 100, x indicates directional bias
    fwmagnitude = y
    LRdiff = x

    #Need to keep return value between -100 and 100, and adjust polarity with logic
    if y>0:
        return max(min(100,fwmagnitude+x/2),-100)
    elif y<=0:
        return max(min(100,fwmagnitude-x/2),-100)
    
def R_mag_calculation(x, y):
    #y indicates amount of forward movement from -100 to 100, x indicates directional bias
    fwmagnitude = y
    LRdiff = x
    
    #Need to keep return value between -100 and 100, and adjust polarity with logic
    if y>0:
        return max(min(100,fwmagnitude-x/2),-100)
    elif y<=0:
        return max(min(100,fwmagnitude+x/2),-100)

    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

#cleanup procedure
GPIO.cleanup()
SPWM.cleanup()