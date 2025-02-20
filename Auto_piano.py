# quais são os passos manuais que devo transformar em código
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1041,379, duration=1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(949,330, (0, 0, 0)):
        click(949,330)
    if pyautogui.pixelMatchesColor(1012,325, (0, 0, 0)):
        click(1012,325)
    if pyautogui.pixelMatchesColor(1078,324, (0, 0, 0)):
        click(1078,324)
    if pyautogui.pixelMatchesColor(1134,322, (0, 0, 0)):
        click(1134,322)