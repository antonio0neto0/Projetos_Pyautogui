import webbrowser
import pyautogui
from time import sleep

# Opção 1 (descomentar a opção desejada)
telefones = [5513996864551]
# Opção 2 (descomentar a opção desejada)
# telefones = []
# with open('fones.txt','r') as arquivo:
#     for linha in arquivo:
#         telefones.append(linha.split('\n'[0]))

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(696,360,duration=1)
    pyautogui.click(760,223,duration=1)
    sleep(10)
    pyautogui.typewrite('Gostaria de participar do nosso evento?(digite sim, se gostaria de participar.')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)