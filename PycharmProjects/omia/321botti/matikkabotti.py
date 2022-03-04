from PIL import ImageGrab, ImageOps
from time import sleep
import pyautogui
import pytesseract

print("press ctrl + c to quit")
"""
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + '    Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        sleep(1)
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
"""
class coordinates():
    StartButton = (640, 1227)
    One = (644, 897)
    Two = (644, 1030)
    Three = (644, 1164)
    Box = (130, 660, 1100, 786)

def restart():
    pyautogui.click(coordinates.StartButton)
    sleep(0.5)

def image():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    kuva = ImageGrab.grab(coordinates.Box)
    bw = kuva.convert('L')
    bw1 = ImageOps.invert(bw)
    bw2 = bw.convert('1')
    # bw.show()
    # print(pytesseract.image_to_string(bw, config='--psm 14'))
    luvut = pytesseract.image_to_string(bw1,
                                      config="-c tessedit" "_char_whitelist=123=-+?")
    print(luvut)
    numerot = luvut[:-2]
    lukuina = numerot.strip(".,'\n")
    lasku = eval(lukuina)
    print(lasku)
    if lasku == 1:
        pyautogui.click(coordinates.One)
        sleep(0.2)
    elif lasku == 2:
        pyautogui.click(coordinates.Two)
        sleep(0.2)
    elif lasku == 3:
        pyautogui.click(coordinates.Three)
        sleep(0.2)



def main():

    try:
        restart()
        while True:
            image()
            sleep(1)
    except KeyboardInterrupt:
        quit()


main()