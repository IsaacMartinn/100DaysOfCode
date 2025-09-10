from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

PHONE_NUM = os.environ("PHONE_NUM")
PASS = os.environ("PASS")

URL = "https://www.tinder.com"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

sleep(2)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

sleep(2)
login = driver.find_element(By.XPATH,value='//*[@id="t41619109"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login.click()

sleep(2)
login_facebook = driver.find_element(By.XPATH,value='//*[@id="t-1686761967"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
login_facebook.click()

#switching to fb window
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

phone_num_login = driver.find_element(By.NAME, "email")
phone_num_login.send_keys(PHONE_NUM)

sleep(2)
fb_pass_login = driver.find_element(By.NAME, "pass")
fb_pass_login.send_keys(PASS, Keys.ENTER)

#switching back to base window
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)
print(driver.title)

sleep(10)

#Allow Location Button
allow_location_button = driver.find_element(By.XPATH,
                                            value='//*[@id="t-1686761967"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]/div')
allow_location_button.click()

#notification button --not sure if this one works yet 
notify_button = driver.find_element(By.XPATH,
                                    value='//*[@id="t-1686761967"]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]/div')
notify_button.click()

cookies_button = driver.find_element(By.XPATH,
                                     value='//*[@id="t41619109"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
cookies_button.click()

sleep(10)
swipe_count = 0

while swipe_count != 100:
    like_button = driver.find_element(by=By.TAG_NAME, value="body")
    like_button.send_keys(Keys.ARROW_RIGHT)
    swipe_count += 1
    sleep(1)