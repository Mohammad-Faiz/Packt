# Design a test that will click browse In the top nav, then click view all books. 
# This should take you to the browse page. 
# 
# Click to clear any filters that are already set, and then click to set the 2021 filter for publication date. 
# Following on from this, automate a test that will type the following words into the search bar, and
# check that all titles found include that search text. 
# Python 
# Paint 
# Secure 
# Tableau

import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

#driver
driver = webdriver.Chrome(executable_path="chromedriver-win64/chromedriver.exe")
driver.get("https://subscription.packtpub.com/login")

#Verifying title of the page
title = driver.title
if title == "Login | Packt Subscription":
    print("Login Page loaded successfully")
else:
    print("Login page does not loaded successfully")

driver.maximize_window()

#Login to Packt
driver.find_element_by_id("login-input-email").send_keys("faiz999888777@gmail.com")
time.sleep(2)
driver.find_element_by_id("login-input-password").send_keys("Qfaiz@1z")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='login-form']/form/button[1]/span").click()
time.sleep(5)
print("Logged in successfully")
time.sleep(5)


#Cl̥ick browse
driver.find_element_by_xpath("//*[@id='packt-navbar']/div[1]/a").click()
print(driver.title) #Print title of the page
time.sleep(5)

#clear filter
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/button[1]").click()
time.sleep(5)


#select filter
publication_date = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[4]/div[1]/div[1]")
time.sleep(5)
dropdown=Select(publication_date)
dropdown.select_by_index(3)

driver.quit()