from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# driver.close()
# driver.quit()

# time.sleep(5)
# price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction").text
# print(f"{price_dollar}.{price_cents}")

# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID,value="submit")
# print(button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH,value="xxxx") if all else fails

event_times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n]={
        "time": event_times[n].text,
        "name": event_names[n].text
    }



driver.quit()

