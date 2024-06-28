from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('www.google.com')
action = ActionChains(driver)
action.send_keys('Sabin Shrestha')
action.send_keys(Keys.ENTER)



time.sleep(10)
driver.quit()

