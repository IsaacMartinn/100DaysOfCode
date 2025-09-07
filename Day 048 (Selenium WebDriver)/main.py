from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://ozh.github.io/cookieclicker/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(3)

game_on = True
cookie = driver.find_element(By.ID,value="bigCookie")

start = time.time()

while game_on:
    cookie.click()
    if time.time() - start >= 5:
        print("5 seconds have passed")
        start = time.time()
        add_ons_list = driver.find_elements(By.CSS_SELECTOR,"#products .unlocked.enabled")
        add_ons_list[-1].click()
        
        
        