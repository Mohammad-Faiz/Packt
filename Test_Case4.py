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

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.support .wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[5]/div[1]/div[1]/button[1]").click()
time.sleep(5)
#select filter
publication_date = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='header'])[3]")))
if publication_date.is_enabled():
    publication_date.click()
    time.sleep(5)
    year =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//div[normalize-space()='2021'])[1]")))
    if year.is_enabled():
        year.click()
        time.sleep(5)
# Check keywords in search bar
Searchbar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@name='query'])[1]")))
if Searchbar.is_enabled():
    Searchbar.click()
    Searchbar.send_keys("Python")
    time.sleep(5)
    Search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-search'])[1]")))
    if Search.is_enabled():
        Search.click()
        time.sleep(5)
    Searchfilter= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Search titles …'])[2]")))
    value = Searchfilter.get_attribute("value")
    print(value)

    if value == 'Python':
        print('Keyword applied successfully')
    else:
        print(" Keyword not applied")

Searchbar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@name='query'])[1]")))
if Searchbar.is_enabled():
    Searchbar.click()
    Searchbar.send_keys("Paint")
    time.sleep(5)
    Search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-search'])[1]")))
    if Search.is_enabled():
        Search.click()
        time.sleep(5)
    Searchfilter= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Search titles …'])[2]")))
    value = Searchfilter.get_attribute("value")
    print(value)

    if value == 'Paint':
        print('Keyword applied successfully')
    else:
        print(" Keyword not applied")

Searchbar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@name='query'])[1]")))
if Searchbar.is_enabled():
    Searchbar.click()
    Searchbar.send_keys("Secure")
    time.sleep(5)
    Search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-search'])[1]")))
    if Search.is_enabled():
        Search.click()
        time.sleep(5)
    Searchfilter= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Search titles …'])[2]")))
    value = Searchfilter.get_attribute("value")
    print(value)

    if value == 'Secure':
        print('Keyword applied successfully')
    else:
        print(" Keyword not applied")
Searchbar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@name='query'])[1]")))
if Searchbar.is_enabled():
    Searchbar.click()
    Searchbar.send_keys("Tableau")
    time.sleep(5)
    Search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-search'])[1]")))
    if Search.is_enabled():
        Search.click()
        time.sleep(5)
    Searchfilter= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Search titles …'])[2]")))
    value = Searchfilter.get_attribute("value")
    print(value)

    if value == 'Tableau':
        print('Keyword applied successfully')
    else:
        print(" Keyword not applied")

driver.quit()