from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support.wait import WebDriverWait


GYM_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = "isaac@test.com"
ACCOUNT_PASSWORD = "isaac123!"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

time.sleep(2)
join_today_button = driver.find_element(By.CLASS_NAME,value="Home_heroButton__3eeI3")
join_today_button.click()

email_field = driver.find_element(By.NAME,value="email")
email_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(By.NAME,value="password")
password_field.send_keys(ACCOUNT_PASSWORD,Keys.ENTER)
time.sleep(2)


#------------------- Step 3 ---------------------------------

class_cards = driver.find_elements(By.XPATH,value="div[id^='class-card-']")

# for card in class_cards:
#     day_group
# # driver.quit()



