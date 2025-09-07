from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://secure-retreat-92358.herokuapp.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

first_name = driver.find_element(By.NAME,"fName")
first_name.send_keys("Isaac")

last_name = driver.find_element(By.NAME,"lName")
last_name.send_keys("Martin")

email_address = driver.find_element(By.NAME,"email")
email_address.send_keys("isaac@email.com",Keys.ENTER)



time.sleep(5)
driver.quit()