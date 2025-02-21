# bot de envio de mensagens em massa para varias pessoas 
# eu posso usar esse link para enviar mensagem direto para o numero desejado:
# https://api.whatsapp.com/send?phone=(numero do telefone)

import pyautogui as pui
import pyautogui
import webbrowser
from time import sleep
import pyperclip

# Numeros que serão enviados as mensagens e a mensagem
telefones = []
telefones_selecionados = ''
mensagem = ''

# Loop para inserir os numeros -----------------------
while telefones_selecionados == '' or telefones_selecionados.isspace():
    telefones_selecionados = pui.prompt(
        title='Atenção', 
        text='Insira os números a ser enviado as mensagens. Não utilize PONTUAÇÃO, ESPAÇOS (utilize somente para separar um contato do outro) ou qualquer outra coisa. Inclua DDD'
        )

# Condcional em caso de cancelamento ou campo em branco
    if telefones_selecionados is None:
        pui.alert(
            title='ATENÇÃO', 
            text='Automação cancelada com sucesso!'
        )
        exit()

    if telefones_selecionados == '' or telefones_selecionados.isspace():
        pui.alert(
            title='ATENÇÃO',
            text='Este campo não pode ficar em branco'
        )

# Loop para a mensagem -------------------
while mensagem == '' or mensagem.isspace():
    mensagem = pui.prompt(
        title='MENSAGEM',
        text='Insira aqui a mensagem a ser enviada:'
    )
# Condicionais das mensagens:
    if mensagem == '' or mensagem.isspace():
        pui.alert(
            title='ATENÇÃO',
            text='Este campo não pode ficar em branco!'
        )

    elif mensagem is None:
        pui.alert(
            title='CANCELADO!',
            text='Automação cancelada com sucesso!'
        )
        exit()
# Separando os numeros selecionados e passando para a variavel   
telefones = telefones_selecionados.split()

# Função para escrever a mensagem
def escrever_mensagem(mensagem_funcao):
    pyperclip.copy(mensagem_funcao)
    pui.hotkey('ctrl', 'v')
    pui.press('enter')

# Enviando as mensagens
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(5)
    pyautogui.click(696,360,duration=1)
    pyautogui.click(760,223,duration=1)
    sleep(5)
    escrever_mensagem(mensagem)
    sleep(5)
    pyautogui.press('enter')
    sleep(300)