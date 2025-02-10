#Automatiza a inserção de login e senha no site da Amazon dentro da tela de login.

import pyautogui
from time import sleep
# Navegar e clicar no campo e-mail.
pyautogui.click(932,290,duration = 2)
sleep(1.5)
#Digitar e-mail.
pyautogui.typewrite('teste@teste.com')
sleep(1.5)
# Apertar tab.
pyautogui.press('tab')
sleep(1.5)
pyautogui.click(1018,333, duration = 2)
sleep(1.5)
# Digitar minha senha.
pyautogui.typewrite('123@4567')
sleep(1.5)
# Apertar tab.
pyautogui.press('tab')
# Apertar espaço.
pyautogui.press('space')