from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USER = os.environ.get("twitter_username")
TWITTER_PASSWORD = os.environ.get("twitter_password")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url="https://www.speedtest.net/")

        sleep(5)
        self.button = self.driver.find_element(By.XPATH,
                                               value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '1]/a/span[4]')
        self.button.click()

        #getting upload and download internet speed
        sleep(50)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                       '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url="https://x.com/i/flow/login")

        #Entering twitter username and password information
        sleep(5)
        self.username = self.driver.find_element(By.NAME, "text")
        self.username.send_keys(f"{TWITTER_USER}", Keys.ENTER)
        sleep(5)
        self.password = self.driver.find_element(By.NAME, "password")
        self.password.send_keys(f"{TWITTER_PASSWORD}", Keys.ENTER)

        sleep(5)
        self.create_tweet = self.driver.find_element(By.XPATH,
                                                     '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        self.create_tweet.click()

        sleep(5)
        self.tweet_text = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        self.tweet_text.send_keys(f'{self.message}')

        # Submitting Post
        self.post = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
        self.post.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
