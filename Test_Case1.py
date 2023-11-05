#To check that all elements on screen are correct, such as positioning, colour, text etc.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#driver
driver = webdriver.Chrome(executable_path="C:/Users/faiz/Desktop/Packt/chromedriver-win64/chromedriver.exe")
driver.get("https://subscription.packtpub.com/login")
driver.maximize_window()

#Verifying title of the page
title = driver.title
if title == "Login | Packt Subscription":
    print("Login Page loaded successfully")
else:
    print("Login page not loaded")

#Login to Packt
driver.find_element_by_id("login-input-email").send_keys("faiz999888777@gmail.com")
time.sleep(2)
driver.find_element_by_id("login-input-password").send_keys("Qfaiz@1z")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='login-form']/form/button[1]/span").click()
print("Logged in successfully")
time.sleep(12)

#Verifying color of background
element = driver.find_element_by_xpath("//nav[1]")
time.sleep(10)
background_color = element.value_of_css_property('background-color')
#print('Background Color:', background_color)
rgb_values = background_color.strip('rgba()').split(',')
hex_color = "#{:02X}{:02X}{:02X}".format(int(rgb_values[0]), int(rgb_values[1]), int(rgb_values[2]))
if hex_color == "#FFFFFF":
    print("Background color matched successfully")
else:
    print("Background color not matched")
time.sleep(5)


#verifying text
element=driver.find_element_by_xpath("//h2[@class='suggested_title']")
time.sleep(5)
element_text = element.text
if element_text == "Your Suggested Titles":
    print("Text matched successfully")
else:
    print("Text is not available")
time.sleep(5)


#To check the position of the element
element = driver.find_element_by_xpath("//*[@id='packt-navbar']/div[2]/a/div/button")  
time.sleep(10)
element_position = element.location 
x = element_position['x'] 
y = element_position['y'] 
#print('Element Position (X, Y):', x, y)
time.sleep(5)
if x == 326 and y == 15:
    print("Position matched successfully")
else:
    print("Position not matched")


driver.quit()