#To check that all elements on screen are correct, such as positioning, colour, text etc.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

#driver
driver = webdriver.Chrome(executable_path="chromedriver-win64/chromedriver.exe")

driver.get("https://subscription.packtpub.com/login")
title = driver.title

if title == "Login | Packt Subscription":
    print("Login Page loaded successfully")
else:
    print("Login page does not loaded successfully")

driver.maximize_window()ś
time.sleep(2)

driver.find_element_by_id("login-input-email").send_keys("faiz999888777@gmail.com")
time.sleep(2)
driver.find_element_by_id("login-input-password").send_keys("Qfaiz@1z")
time.sleep(2)
driver.find_element_by_xpath("//*[@id="login-form"]/form/button[1]/span").click()

driver.quit()
