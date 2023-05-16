# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
import neopixel
import touchio
import random

pixel_pin = board.A1
num_pixels = 30

touchpad0 = board.A0 
touchpad2 = board.A2 

touch0 = touchio.TouchIn(touchpad0)
touch2 = touchio.TouchIn(touchpad2)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

from morse import *

def showtext(msg):
    code = encryption(msg)
    for x in range(len (code)):
        clr = blank
        if code[x] == '.':
            clr = dtc
        if code[x] == '-':
            clr = dc
        pixels[0] = clr
        pixels.show()
        for i in range(num_pixels-1):
            pos = num_pixels -1 - i
            pixels[pos]=pixels[pos-1]
        pixels[0]=blank
        pixels.show()
        time.sleep(.25)
        
def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def douse( wait):
    for i in range(num_pixels):
        pixels[num_pixels - i -1] = blank
        time.sleep(wait)
        pixels.show()
    time.sleep(0.1)



blank = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
KYLO = (254,0,0)
DARTH = (0,0,255)
WHITE = (255,255,255)


blades = [RED,YELLOW,GREEN,CYAN,BLUE,PURPLE,DARTH,WHITE,KYLO]

bnum = 3

lit = False
done = False

blade = blades[bnum]
ACTIVE = blade
showtext("may the force be with you")

while not done:
    blade = blades[bnum]
    Val = 0
    
    if touch0.value:
        Val = Val + 1
    if touch2.value:
        Val = Val + 2
    
    if Val == 1:
        if lit:
            douse(.02)
            lit = False
        bnum = bnum + 1
        pixels.fill(blank)
        pixels.show()
        if bnum > 7:
            bnum = 0
        
        pixels[0] = blades[bnum]
        pixels.show()
        ACTIVE = blank
        
    if Val == 3:
        done = True
        
    if Val == 2:
        if lit:
            douse(.02)
            lit = False
        else:
            color_chase(blades[bnum],.01)
            ACTIVE = blades[bnum]
            lit = True
            
    if ACTIVE == KYLO and lit: #sparks
        pixels.fill(KYLO)
        for s in range(random.randrange(7)):
            pixels[random.randrange(num_pixels)] = YELLOW
            pixels.show()
            time.sleep(.005)

    if ACTIVE == DARTH and lit: #sparks
        pixels.fill(DARTH)
        for s in range(random.randrange(7)):
            pixels[random.randrange(num_pixels)] = WHITE
            pixels.show()
  
    time.sleep(.25)
    
