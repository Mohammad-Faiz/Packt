
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#driver
driver = webdriver.Chrome(executable_path="chromedriver-win64/chromedriver.exe")
driver.get("https://subscription.packtpub.com/login")
driver.maximize_window()

#Verifying title of the page
title = driver.title
if title == "Login | Packt Subscription":
    print("Login Page loaded successfully")
else:
    print("Login page does not loaded successfully")

#Login to Packt
driver.find_element_by_id("login-input-email").send_keys("faiz999888777@gmail.com")
time.sleep(2)
driver.find_element_by_id("login-input-password").send_keys("Qfaiz@1z")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='login-form']/form/button[1]/span").click()
time.sleep(5)
print("Logged in successfully")


# #verifying top navigation bar(My library)
lib = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[@id='library-dropdown']")))
if lib.is_enabled():
    lib.click()
    print("successfully switched")
    time.sleep(5)
    Home = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Home']")))
    if Home.is_enabled():
        Home.click()
    title = driver.title
    print(title)
    if title == "Packt Subscription | Advance your knowledge in tech":
        print("Home Page loaded successfully")
    else:
        print("Home page does not loaded successfully")
else:
    print("Home is not enabled")
lib = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='library-dropdown']")))
if lib.is_enabled():
    lib.click()
    time.sleep(5)
    Playlist = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Playlists']")))
    if Playlist.is_enabled():
        Playlist.click()
    title = driver.title
    time.sleep(5)
    print(title)
    if title == "Playlists | Packt Subscription":
        print("Playlists Page loaded successfully")
    else:
        print("Playlists page does not loaded successfully")
else:
    print("Playlists is not enabled")

