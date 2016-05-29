
from floppy import FloppyPlayer,getserial,A,B,C,D,E,F,G
import pygame
import time

import pygame.midi  as midi
from pygame.locals import *

pygame.init()


pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.midi.init()

count = pygame.midi.get_count()
print "counting %s"%count
defaultid = pygame.midi.get_default_input_id()
print "default",defaultid

midin = pygame.midi.Input(3)

ser= getserial() 
fp = FloppyPlayer(ser) 
"""
B 7872
C 7395



F 5400
F# 5170
G 4885
G# 4595
A 4350
A# 
B 3800
C 3500
 3800
 3800
 3800
"""
NOTEMAPPING={
    9 :90454,
    10:84994,
    11:79865,
    12:75044,
    13:70515,
    14:66259,
    15:62260,
    16:58502,
    17:54972,
    18:51654,
    19:48536,
    20:45607,
    21:42854,
    22:40268,
    23:37837,
    24:35554,
    25:33408,
    26:31392,
    27:29497,
    28:27717,
    29:26044,
    30:24472,
    31:22995,
    32:21607,
    33:20303,
    34:19078,
    35:17926,
    36:16844,
    37:15828,
    38:14872,
    39:13975,
    40:13131,
    41:12339,
    42:11594,
    43:10894,
    44:10237,
    45:9619,
    46:9038,
    47:8493,
    48:7980,
    49:7499,
    50:7046,
    51:6621,
    52:6221,
    53:5846,
    54:5493,
    55:5161,
    56:4850,
    57:4557,
    58:4282,
    59:4024,
    60:3781,
    61:3553,
    62:3338,
    63:3137,
    64:2947,
    65:2770,
    66:2602,
    67:2445,
    68:2298,
    69:2159,
    70:2029,
    71:1906,
    72:1791,
}


#NOTEMAPPING = {
#    60:C,
#    61:C,
#    62:D,
#    62:D,
#    63:E,
#    64:F,
#    65:F,
#    66:G,
#    67:G,
#
#    }
STEPSIZE = 2
def treat(item,fp,currentnote):
    

    info,time = item
    code,note,vel,some = info
    #print "t %s: code %s , note %s , vel %s"%(time,code,note,vel)

    if code == 128:
        # releve
        #for i in range(6):
        #    fp.sendSound(i,0)
        fp.stopNote(NOTEMAPPING[note])
         
    elif code == 144:
        # appuye
        if note >=9 and note <= 72:
            #for i in range(6):
            #    fp.sendSound(i,NOTEMAPPING[note])


            fp.playNote(NOTEMAPPING[note])
            print NOTEMAPPING[note], vel




        #if note == 48:
        #    currentnote += STEPSIZE
        #    fp.sendSound(0,currentnote)
        #    print currentnote
        #elif note == 50:
        #    currentnote -= STEPSIZE
        #    fp.sendSound(0,currentnote)
        #    print currentnote
        #elif note == 49:
        #    fp.sendSound(0,currentnote)

        #    print currentnote

    return currentnote
currentnote = 7500
while True: 

    if midin.poll():
        data = midin.read(10)
        for item in data:
            currentnote = treat(item,fp,currentnote)



print "end"
#
#for i in range(count):
#    try:
#        midi = pygame.midi.Input(i)
#    except MidiException as e:
#        print "error for %s"%i
#    except Exception as e:
#        print "unknow error for %s"%i
#


