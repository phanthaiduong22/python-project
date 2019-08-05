from PIL import Image
import pyautogui
import time
import cv2
import pytesseract


# im = Image.open("sampple1.jpg")
# text = pytesseract.image_to_string(im,lang = 'eng')
# print(text)
class Cordinates():
    textbox = (80, 275)
    replayBtn = (800,450)
    whereitype = (250,460)
def restartGame():
    pyautogui.click(Cordinates.replayBtn)


# width = 850
# heigh=105
# time.sleep(2)
#
# print(pyautogui.locateOnScreen('test1.png'))

# im = Image.open('test1.png')

def main():
    restartGame()
    time.sleep(0.5)
    pyautogui.click(Cordinates.whereitype)
    while True:
        pyautogui.screenshot('image.png')
        img = cv2.imread("image.png")
        crop_image = img[320:370, 80:940]
        cv2.imshow("cropped", crop_image)
        cv2.imwrite('cropped.png',crop_image)
        text = pytesseract.image_to_string(crop_image, lang='eng')
        for c in text:
            print(c)
            if c == 'enter':
                    c=' '
            pyautogui.press(c)
            if pyautogui.position() == (1, 1):
                exit()
        pyautogui.press(' ')

main()
