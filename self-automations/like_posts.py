import pyautogui
import time

pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

time.sleep(1)
pyautogui.write('https://x.com/home') 
pyautogui.press('enter')

time.sleep(3)


pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(2)

pyautogui.press('/')

pyautogui.write('#LSPPDay26')
pyautogui.press('enter')

pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')


time.sleep(3)
pyautogui.press('j')

for i in range(1, 200):
  pyautogui.press('j')
  time.sleep(0.5)
  pyautogui.press('l')
  

















