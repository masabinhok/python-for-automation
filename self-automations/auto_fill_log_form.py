# This is a pyautogui automated script to fill out the daily log form for leapfrog learning challange.

#You might need to edit some tab presses according to your device.

#Do star the repo if it helps.

# You should have python installed in your computer.

#In your terminal, type 'pip install pyautogui' to install the pyautogui module.
#Importing pyautgui responsible for gui automation, i.e mouse keyboard.
import pyautogui

# importing time for sleeping (delay purpose) in-build module
import time

# it opens the browser, you can edit your browser name on line here.
pyautogui.press('win') #This opens windows
pyautogui.write('brave') #here (this types brave)
pyautogui.press('enter') #this presses enter.

time.sleep(0.5) #delay

# opens twitter,
pyautogui.write('https://x.com/home')
pyautogui.press('enter')


time.sleep(2) #delay

# navigates to profile
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(3)#delay

#navigates to share button, you can edit the number of tabs to navigate to the desired position.
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')


time.sleep(0.5)#delay

#Clicks on the share button and copies the link to the keyboard for the latest upload.
pyautogui.press('enter')  
pyautogui.press('enter')  


# Link is copied, lets open the google form with its link.

time.sleep(1) #delay

#opening a new tab
pyautogui.hotkey('ctrl', 't')

#navigating to google form
pyautogui.write('https://docs.google.com/forms/d/e/1FAIpQLSfZB4Cnh1EZvuS6GweEYM-RnuUOrj0miTTfi5bdfkVvkxbeRg/viewform?pli=1&pli=1')
pyautogui.press('enter')

time.sleep(3)#delay

#record email
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('space')

time.sleep(0.5)#delay


#set todays date
pyautogui.press('tab')
pyautogui.press('space')
pyautogui.press('enter')



time.sleep(0.5)#delay

#navigate to twitter username
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

#write username, please change it to your username...
pyautogui.write('ersabinshrestha') #edittt


time.sleep(0.5)#delay

#navigate to twitter post link
pyautogui.press('tab') 

#paste the copied link
pyautogui.hotkey('ctrl', 'v')

# submit the form
pyautogui.press('tab')
pyautogui.press('space')







