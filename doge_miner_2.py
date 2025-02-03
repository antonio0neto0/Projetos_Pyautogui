import pyautogui
from time import sleep

'''o jogo pé o doge miner 2''' '''o jogo foi deixado na metade da tela a direita'''

pyautogui.moveTo(1009,327,duration=1)
for i in range(100):
    sleep(0.5)
    pyautogui.click()
    