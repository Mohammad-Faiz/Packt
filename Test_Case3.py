from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#driver
driver = webdriver.Chrome(executable_path="C:/Users/faiz/Desktop/Packt/chromedriver-win64/chromedriver.exe")
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

time.sleep(15)


#capturing title of home page
Home_title=driver.title

#click on edit preference
driver.find_element_by_xpath("/html/body/div[1]/div/main/section[2]/div[2]/h5/a").click()

#capturing title of edit preference page
edit_title=driver.title

time.sleep(5)

#compare Title of Home and Edit page
if Home_title == edit_title:
    print("Title Matched successfully")
else:
    print("Title not matched")

driver.quit()
