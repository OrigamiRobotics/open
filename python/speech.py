import paho.mqtt.client as mqtt
from hostdef import *
from subprocess import call

speed = "150"   #Default speaking speed

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("romibo/speech",0)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg_raw):
    msg = msg_raw.payload.rstrip('\t\r\n\0').split('||')                                        #Split rate data and speech data
    print(msg_raw.topic+" "+msg[0]+" "+msg[1])                                                  #Debug
    speech_rate = 100+(int)(float(msg[0])*100)                                                  #processing speech rate to fit espeak
    call(["espeak", "-ven+f3", "-k5", "-s"+str(speech_rate), str(msg[1]), "shell=True"])        #calling espeak

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()