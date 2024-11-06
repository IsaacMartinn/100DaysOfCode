import requests
from bs4 import BeautifulSoup
import smtplib
import re
from dotenv import load_dotenv
import os

load_dotenv(".env")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
STMP_ADDRESS = os.getenv("STMP_ADDRESS")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",

}

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.ca/Instant-Electric-Pressure-Sterilizer-Stainless/dp/B00FLYWNYQ/ref=sr_1_2?crid=3BTAEW4510SLC&dib=eyJ2IjoiMSJ9.5s_5RS4qKJMOxc04dnxdoss-L7XfL35kgkFImE1NyQPrw0gwweOVbJQ185xb3RHVuFlnZA_diDdwRe0P5B66A1xlJlM_fIRKJjIM77947NDJU0Y0_LRXI8IUkzG5w_BaYKKks9mfRNpHQJDJQcOXgJJIolhEqz1V6wftotV2j71SRVo5w757AUJGAyEY38IWS7t9bwy6VCSUdKDfENB6uUwTXEoaj3qPtfbaOYLczpZ_fMhYOIQBHesE_qr5qsWBMEriZbjHzEw8KUT8To7JxrxVAzLGpNOtzUJvOFfWhTM.XM7CIhdRza2R0T7MijZrIcXavtaiKe2xzS16zah3GY0&dib_tag=se&keywords=Instant+Pot+Duo+Plus+9-in-1+Electric+Pressure+Cooker%2C+Slow+Cooker%2C+Rice+Cooker%2C+Steamer%2C+Saut%C3%A9%2C+Yogurt+Maker%2C+Warmer+%26+Sterilizer%2C+Includes+App+With+Over+800+Recipes%2C+Stainless+Steel%2C+3+Quart&qid=1720821143&sprefix=instant+pot+duo+plus+9-in-1+electric+pressure+cooker%2C+slow+cooker%2C+rice+cooker%2C+steamer%2C+saut%C3%A9%2C+yogurt+maker%2C+warmer+%26+sterilizer%2C+includes+app+with+over+800+recipes%2C+stainless+steel%2C+3+quart%2Caps%2C134&sr=8-2"

response = requests.get(url=live_url, headers=headers)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "html.parser")
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
whole_number = int(price)
title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText().strip()

clean_title = re.sub(r'\s+', ' ', title)

BUY_PRICE = 100

if whole_number < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS,
                            to_addrs=EMAIL_ADDRESS,
                            msg=f"Subject:Amazon Price Alert \n\n{clean_title} is now {price}".encode('utf-8')
                            )
