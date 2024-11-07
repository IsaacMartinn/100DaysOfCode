from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
cookie_cost = driver.find_elements(By.CSS_SELECTOR, value="body div div div b")[1::]

#store items
items = driver.find_elements(by=By.CSS_SELECTOR,value="#store div")
items_id = [item.get_attribute("id") for item in items]
# print(items_id)

cost_list = []
for x in cookie_cost:
    cost_list.append(x.text.split("-"))

#all prices placed in all_cost
all_list = cost_list[0:8]
all_cost = [int(item[1].replace(',', "").strip()) for item in all_list]


timeout = time.time() + 5  #time 5 seconds from now
five_min = time.time() + (5*60) # time 5 min from now

cps = driver.find_element(By.ID,"cps").text

while True:
    cookie.click()
    current_cookie_money = driver.find_element(By.ID, value="money").text.replace(',', "").strip()
    cookie_money = int(current_cookie_money)
    if time.time() > timeout:
        result = [num for num in all_cost if cookie_money >= num]
        highest_value_item_index = result.index(max(result))

        # print(f"#{items_id[highest_value_item_index]}")
        x = driver.find_element(By.ID, f"{items_id[highest_value_item_index]}")
        x.click()
        timeout = time.time() + 5
    if time.time() > five_min:
        print(f"{cps}")
        break

# driver.quit()