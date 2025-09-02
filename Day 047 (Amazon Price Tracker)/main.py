from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "sec-fetch-dest":"document",
    "sec-fetch-site":"cross-site",
    "sec-fetch-mode":"navigate",
    "sec-fetch-dest":"?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

URL = "https://appbrewery.github.io/instant_pot/"
# URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(url=URL,headers=header)
product_web_page = response.text

soup = BeautifulSoup(product_web_page,"html.parser")
price = soup.find(name="p",class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice").getText().strip().split('$')[1]
product_title = soup.find(name="span", id="productTitle").getText()
clean_title = " ".join(product_title.split()).replace(",", "")


if float(price) < 100:
    message = f"{clean_title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )


