import pyautogui
from time import sleep

email = pyautogui.prompt(text = 'Digite seu e-mail',title = 'informações obrigatórias')
senha = pyautogui.password(text = 'Digite sua senha:',title = 'Dados de login',mask='*')
pyautogui.click(860,64, duration = 2)
pyautogui.typewrite(email)
sleep(1.5)
pyautogui.press('enter')
sleep(1.5)
pyautogui.typewrite(senha)
sleep(1.5)
pyautogui.press('enter')
