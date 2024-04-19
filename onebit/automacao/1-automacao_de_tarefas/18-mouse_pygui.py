# Automatizando o mouse com o PyAutoGUI

import pyautogui
import time

# 1 -> Descobrindo o tamanho da tela (1368x768  )
print(pyautogui.size())

# 2 -> Pegar a posicação atual do mouse
print(pyautogui.position())

# 3 -> App para pegar a posição do mouse em tempo real
# from pyautogui import mouseInfo
# python3(linux)
# mouseInfo()
# No meu precisei instalar o scrolt, algo assim, e usar:
# import mouseinfo
# >>> mouseinfo.MouseInfoWindow()

# 4 -> Mover o cursor do mouse
pyautogui.moveTo(1281,47,1) # -> Coordenada X e Y e o tempo que demora até o mouse chegar lá
# time.sleep(1.5)
pyautogui.click()

# 5 -> Realizando o scroll
pyautogui.moveTo(652,508)
pyautogui.click()
time.sleep(1.5)
pyautogui.scroll(1) # Se o número é positivo scrolla pra cima, negativo pra baixo. Quanto menor, menos scrolla