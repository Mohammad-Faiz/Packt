#To check that all elements on screen are correct, such as positioning, colour, text etc.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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


# #Verifying color
# element = driver.find_element_by_id('packt-navbar')
# background_color = element.value_of_css_property('background-color')
# print('Background Color:', background_color)
# # hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b, a)


# #verifying text
element=driver.find_element(By.XPATH,"//*[@id='packt-navbar']/div[4]/a[3]")
element_text = element.text
print(f"Element Text='{element_text}'")
time.sleep(2)
# if element_text == "Your Suggested Titles":
#     print("Text availaibility is right")
# else:
#     print("Text is not available")
#color: #6d737d;
driver.quit()


# #to convert rbga to hexadecimal
# rgb_values = background_color_rgb.strip('rgba()').split(',') 
# hex_color = "#{:02X}{:02X}{:02X}".format(int(rgb_values[0]), int(rgb_values[1]), int(rgb_values[2]))


#to check the position of the element
#element = driver.find_element_by_id('element_id')  
# Replace with the appropriate method to locate your element 
# Get the element's position element_position = element.location 
# Extract X and Y coordinates x = element_position['x'] y = element_position['y'] 
# Print the element's position print('Element Position (X, Y):', x, y)