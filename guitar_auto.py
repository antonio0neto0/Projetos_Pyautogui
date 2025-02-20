import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(975,621,(0,152,0)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1060,619,(255,0,0)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1147,618,(244,244,2)):
        pyautogui.press('j')
        sleep(0.05)