'''DESAFIO
1) Navegue ate o site htpps://cursoautomacao.netlify.app/
2) encontre e clique no campo "Digite seu nome" dentro de "Exemplos
Alertas" e digite seu nome
3) clicar em alerta, para gerar a alerta 
4) feche a janela
5) suba a pagina totalmente para cima
6) desça apenas o suficiente para conseguir chegar até a secção que contem os arquivos 
para qual Voce ira fazer o dowload deles (no caso 
voce deve fazer essa parte tambem totalmente com pyautogui , nada de processos manuais
) e clicar e movimentar o mouse da maneira que for necessario para baixar os arquivos )
7) depois de ter feito isso , quero que vc crie um alerta que diz 
VOCE TERMINOU!!'''

import webbrowser
import pyautogui
import time

#entrar no site
webbrowser.open('https://cursoautomacao.netlify.app/')

time.sleep(3)
pyautogui.moveTo(1355,158, duration= 2)
pyautogui.scroll(-1990)
time.sleep(1)

#digitar o nome 
pyautogui.click(807,611, duration= 1)
pyautogui.typewrite('Antonio Daniel')
time.sleep(2)

pyautogui.click(798,651, duration= 1)
pyautogui.click(1220,165, duration= 1)

#baixar arquivos
pyautogui.scroll(-1400)
time.sleep(1)

pyautogui.click(849,455, duration= 1)
pyautogui.click(856,571, duration= 1)

#criar alerta 

pyautogui.alert('******VOCE TERMINOU !!!!*******')