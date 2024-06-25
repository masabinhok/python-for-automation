import pyautogui
import time


pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

time.sleep(1)

pyautogui.write('https://github.com/')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')

pyautogui.write('https://x.com/home')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')

pyautogui.write('https://x.com/home')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')

pyautogui.write('https://x.com/home')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')




