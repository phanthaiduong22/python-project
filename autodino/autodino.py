from PIL import Image, ImageOps
import pyscreenshot as ImageGrab
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (475, 450)
    dinosaur = (237,453)
    #x=345 check for tree
    #y=470 check for height
def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSapce():
        pyautogui.keyDown('space')
        #time.sleep(0.005)
        print("Jump")
        pyautogui.keyUp('space')

def imageGrab():
    box = (300,463,360,480)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

# while True:
#     imageGrab()

def main():
    restartGame()
    while True:
        if(imageGrab()!=1267):
           pressSapce()
           #time.sleep(0.05)

main()

