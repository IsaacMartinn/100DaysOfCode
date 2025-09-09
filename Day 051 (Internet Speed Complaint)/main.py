from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_NUM = "4168852667"
USERNAME = "isaacmartinnn"
PASSWORD ="Isaacmax2002"
USERNAME_XPATH = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
PASSWORD_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'


class InternetSpeedTwitterBot():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.upload_speed = 0 
        self.download_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/result/18203886216")
        self.go_button = self.driver.find_element(By.CLASS_NAME, value="start-text").click()
        time.sleep(30)
        self.download_speed = self.driver.find_element(By.CLASS_NAME,value="download-speed").text
        self.upload_speed = self.driver.find_element(By.CLASS_NAME,value="upload-speed").text
        time.sleep(5)
        print(self.download_speed)
        print(self.upload_speed)
        # May not need to add these delays 
        

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login?lang=en")
        time.sleep(3)
        self.username_field = self.driver.find_element(By.XPATH,value=USERNAME_XPATH)
        self.username_field.send_keys(USERNAME,Keys.ENTER)
        time.sleep(3)
        self.password_field = self.driver.find_element(By.NAME,value="password")
        self.password_field.send_keys(PASSWORD,Keys.ENTER)
        time.sleep(4)
       
        self.write_text = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey internet Provider, why is my internet speed {self.download_speed}down/{self.upload_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        self.write_text.send_keys(tweet)
        time.sleep(2)

        self.post_button = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        self.post_button.click()
        time.sleep(10)
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

