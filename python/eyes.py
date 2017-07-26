import Tkinter as tk
import itertools as it
import random
import datetime
import time
from os import listdir

#Make list of .png files used for animation of excited
list = listdir("/home/chip/Romibo-V8/eyes/Romibo excited/")
list.sort()
list_for_romibo_excited=["/home/chip/Romibo-V8/eyes/Romibo excited/"+ i for i in list]


#Make list of .png files used for animation of indifferent
list = listdir("/home/chip/Romibo-V8/eyes/Romibo indifferent/")
list.sort()
list_for_romibo_indifferentShort=["/home/chip/Romibo-V8/eyes/Romibo indifferent/"+ i for i in list]

#reversing blinking1
list2 = ["/home/chip/Romibo-V8/eyes/Romibo indifferent/"+ i for i in list]
list2.sort(reverse=True)
list_for_romibo_indifferentShort=list_for_romibo_indifferentShort+ list2


#Make list of .png files used for animation of blinking
list = listdir("/home/chip/Romibo-V8/eyes/eyelid blink/")
list.sort()
list_for_romibo_eyelidBlink=["/home/chip/Romibo-V8/eyes/eyelid blink/"+ i for i in list]


#reversing blinking2
list2 = ["/home/chip/Romibo-V8/eyes/eyelid blink/"+ i for i in list]
list2.sort(reverse=True)
list_for_romibo_eyelidBlink=list_for_romibo_eyelidBlink+ list2

#make a list of files for animation of curious emotion
list = listdir("/home/chip/Romibo-V8/eyes/Romibo curious/")
list.sort()
list_for_romibo_curious=["/home/chip/Romibo-V8/eyes/Romibo curious/"+ i for i in list]

#debug
#print(list_for_romibo_excited)

count = 0
excited_length = len(list_for_romibo_excited)
indifferentShort_length = len(list_for_romibo_indifferentShort)
blink_length = len(list_for_romibo_eyelidBlink)
curious_length = len(list_for_romibo_curious)

#emotion letters: N = normal, E = excited, I = indifferent short, T = twitterpated
#C = curious
emotion = 'N'
busy = False            #Busyness of system
timestamp = time.time()
blinkInterval = 2 + random.random()*4                     #Set blink interval randomly between 2 to 6 seconds

def animate():
    """ cycle through """
    global emotion
    #If busy == False, check open emotion request file
    if busy == False:
        file = open("/home/chip/Romibo-V8/emotion.txt","r")
        emotion = file.read(1)
        file.close()
 
    if emotion == 'N':
        #turn on auto blink
        auto_blink()
    elif emotion == 'E':
        romibo_excited()
    elif emotion == 'I':  
		romibo_indifferent()
    elif emotion == 'C':
		romibo_curious()
		
    root.after(delay, animate)

def auto_blink():
    global label, timestamp, blinkInterval, busy, count               #To access global variables
    print (label["image"])
    if time.time()>(timestamp + blinkInterval):                     #If time is more than blink interval, trigger blink sequence
        busy = True
        if count<blink_length:
            img = next(romibo_eyelidBlink_pictures)                     #Obtain name of next image in list
            #change image in placeholder
            label["image"] = img                                    #Change image in placeholder
            count = count+1
        elif count == blink_length:
            label["image"] = romibo_normal_picture
            count = 0
            busy = False
            timestamp = time.time()
            blinkInterval = 2 + random.random()*4                       #Set blink interval randomly between 2 to 6 seconds

def romibo_excited():
    global label, timestamp, blinkInterval, busy, count
    if count<excited_length:
        busy = True
        img = next(romibo_excited_pictures)                     #Obtain name of next image in list
        #change image in placeholder
        label["image"] = img                                    #Change image in placeholder
        print(img)
        count = count+1
    if count == excited_length:
        count = 0
        busy = False
        label["image"] = romibo_normal_picture
        file = open("/home/chip/Romibo-V8/emotion.txt","w")
        file.write("N")
        file.close()
        emotion = 'N'
        timestamp = time.time()
        
		
def romibo_indifferent():
    global label, timestamp, blinkInterval, busy, count
    if count<indifferentShort_length:
        busy = True
        img = next(romibo_indifferentShort_pictures)    		#Obtain name of next image in list
		
        #change image in placeholder
        label["image"] = img                                    #Change image in placeholder
        print(img)
        count = count+1
    if count == indifferentShort_length:
        count = 0
        busy = False
        label["image"] = romibo_normal_picture
        file = open("/home/chip/Romibo-V8/emotion.txt","w")
        file.write("N")
        file.close()
        emotion = 'N'
        timestamp = time.time()
		
            

def romibo_curious():
    global label, timestamp, blinkInterval, busy, count
    if count<curious_length:
        busy = True
        img = next(romibo_curious_pictures)    		#Obtain name of next image in list
		
        #change image in placeholder
        label["image"] = img                                    #Change image in placeholder
        print(img)
        count = count+1
    if count == curious_length:
        count = 0
        busy = False
        label["image"] = romibo_normal_picture
        file = open("emotion.txt","w")
        file.write("N")
        file.close()
        emotion = 'N'
        timestamp = time.time()
		
#Essential function for tkinter
root = tk.Tk()

#Create placeholder(called a widget) to house pictures that change
label = tk.Label(root, bd = 0)

#Position widget
label.place(x=20,y=100)


# store as tk img_objects
romibo_excited_pictures = it.cycle(tk.PhotoImage(file=img_name) for img_name in list_for_romibo_excited)
romibo_indifferentShort_pictures = it.cycle(tk.PhotoImage(file=img_name) for img_name in list_for_romibo_indifferentShort)
romibo_eyelidBlink_pictures = it.cycle(tk.PhotoImage(file=img_name) for img_name in list_for_romibo_eyelidBlink)
#romibo_curious_pictures = it.cycle(tk.PhotoImage(file=img_name) for img_name in list_for_romibo_curious)
romibo_normal_picture = tk.PhotoImage(file="/home/chip/Romibo-V8/romibo_normal_picture.png")


# set initial eyes
label["image"] = romibo_normal_picture

# milliseconds
delay = 40

animate()

#Make GUI black bg and full-screen
root.configure(bg='black')
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget

#Bind escape button
root.bind("<Escape>", lambda e: e.widget.quit())

#To prevent display lag, load images once each
for i in range(0, blink_length):
    img = next(romibo_eyelidBlink_pictures)
    print(img)

for i in range(0, excited_length):
    img = next(romibo_excited_pictures)
    print(img)
for i in range(0, indifferentShort_length):
    img = next(romibo_indifferentShort_pictures)
    print(img)


#for i in range(0, curious_length):
  #  img = next(romibo_curious_pictures)
  #  print(img)
	

root.mainloop()