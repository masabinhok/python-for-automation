from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

driver = webdriver.Chrome()
driver.get("https://www.coursera.org?/authMode=login")



