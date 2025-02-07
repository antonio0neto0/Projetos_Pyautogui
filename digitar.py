import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


pyautogui.click(1067,274,duration=0.5)
pyautogui.moveTo(1176,672,duration=1)
pyautogui.click()
escrever_frase('Olá, Bom Dia!')

# pyautogui.typewrite('Ola Bom Dia!') nao funciona caracteres especiais

pyautogui.click(1319,672,duration=0.5)