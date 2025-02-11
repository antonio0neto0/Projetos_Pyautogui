import pyautogui
import pyperclip

def escrever_senha(senha_copiada):
    pyperclip.copy(senha_copiada)
    pyautogui.hotkey('ctrl', 'v')

def escrever_email(email_copiado):
    pyperclip.copy(email_copiado)
    pyautogui.hotkey('ctrl', 'v')

email=''
while email == '' or email.isspace() == True:
    email = pyautogui.prompt(title='EMAIL', text='Por Favor! Digite seu email:')
    if email == '' or email.isspace():
        pyautogui.alert(title='ATENÇÃO!', text='Digite um email válido para prosseguir!', button='OK')

senha=''
while senha == '' or senha.isspace() == True:
    senha = pyautogui.password(title='SENHA', text='Digite a sua senha:', mask='*')
    if senha == '' or senha.isspace() == True:
        pyautogui.alert(title='ATENÇÃO', text='Digite uma senha válida!')

pyautogui.leftClick(x=1279, y=211, duration=1)
escrever_email(email)
pyautogui.hotkey('enter')
escrever_senha(senha)
pyautogui.hotkey('enter')