import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=ZILLOW_CLONE_URL)
zillow_web_page = response.text
soup = BeautifulSoup(zillow_web_page,"html.parser")

#all housing links
all_links_soup = soup.find_all(name='a',class_="StyledPropertyCardDataArea-anchor")
housing_links = [link.get("href") for link in all_links_soup]

#all housing prices
all_housing_prices_soup = soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
all_house_prices = [price.text.split("+")[0].split("/")[0] for price in all_housing_prices_soup]

#all addresses
all_address_soup = soup.find_all(name="address")
addresses = [address.text.strip().replace("|","") for address in all_address_soup]

###### selenium part########
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSeDKKBMVu0NGtapZnzxm6qcMrVSdXHTuwyvNdIAKktK6uOYwQ/viewform?usp=sf_link")


for i in range(len(housing_links)-1):
    sleep(2)
    #Filling in the address
    fill_in_address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_in_address.send_keys(f'{addresses[i]}')
    #filling in the price
    fill_in_price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_in_price.send_keys(f'{all_house_prices[i]}')
    #filling in the link to house
    fill_in_link = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_in_link.send_keys(f'{housing_links[i]}')

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    sleep(1)
    submit_another_response_button = driver.find_element(By.LINK_TEXT, 'Submit another response')
    submit_another_response_button.click()


#adding it data to google sheets
# driver.get(url="https://docs.google.com/forms/d/17hDmLM6EzgpZGrnyLudwhDQXYdK_6n8ZnFoRlAtCT8Q/edit#responses")
# sleep(2)
# cookies_button = driver.find_element(By.XPATH,'//*[@id="inproduct-guide-modal"]/div[3]/button')
# cookies_button.click()
# sleep(1)
# view_in_sheets_button = driver.find_element(By.XPATH,'//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]')
# view_in_sheets_button.click()
