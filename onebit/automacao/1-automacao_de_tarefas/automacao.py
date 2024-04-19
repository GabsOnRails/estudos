'''
Criando a lógica que iŕa realizar o cadastro automático dos alunos.
O arquivo 'Gui.py' realiza a criação da interface gráfica.
A interface gráfica precisa estar aberta e as coordenadas passadas de acordo
com o respectivo local.
'''

import pyautogui
from time import sleep

pyautogui.moveTo(1281,47,1)
pyautogui.click()

with open("files/alunos.txt", "r", encoding="utf-8") as file:
    for line in file:
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        pyautogui.click(355, 357, duration=1)
        pyautogui.write(aluno)
        pyautogui.click(396, 395, duration=1)
        pyautogui.write(email)
        pyautogui.click(353,420, duration=0.5)
        pyautogui.screenshot(f'files/img/{aluno}.png')
        sleep(1)
    
       