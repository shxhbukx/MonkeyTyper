import pyautogui
import time

time.sleep(4)

text = "The quick brown fox jumps over the lazy dog"

pyautogui.PAUSE = 0.01

charList = [i for i in text]

for char in charList:
    pyautogui.typewrite(char)