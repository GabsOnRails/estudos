# Automatizando o teclado

import pyautogui
import time


# 1 -> Automatizando teclado
# pyautogui.hotkey('alt','tab') # -> Pressiona mais de uma tecla ao mesmo tempo
# time.sleep(1)
# pyautogui.press('winleft') # -> Pressiona uma tecla apenas
# # pyautogui.write('calculadora')
# # pyautogui.press('enter')

# with pyautogui.hold('winleft'): # -> Hold mantém pressionada a tecla
pyautogui.hotkey('win','alt','right')
