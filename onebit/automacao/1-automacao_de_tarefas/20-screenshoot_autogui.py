# Automatizando screenshoot

import pyautogui
import time
from datetime import datetime

# Print da tela inteira
# pyautogui.screenshot('exemplo.png')

# -> Se quiser tirar o print de outra tela é necessário colocar um time.sleep
# pyautogui.moveTo(1281,47,1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.screenshot('exemplo2.png') 
contador = 0
while True:
    pyautogui.screenshot(f'print_{time.time()}.png')
    time.sleep(120)
    contador +=1
    if contador == 2:
        break
