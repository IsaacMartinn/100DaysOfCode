from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

num = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(num.text)
driver.quit()

#Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT,value="Content portals")
# all_portals.click()

#Find the "Search" <input> by Name
# search=driver.find_element(By.NAME,value="search")
# search.send_keys("Python")

#Sending keyboard input to selenium 
# search.send_keys("Python",Keys.ENTER)

