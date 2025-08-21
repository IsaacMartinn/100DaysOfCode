import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt", encoding="utf-8") as file:   # ensure UTF-8 read
        contents = file.readlines()
        random_num = random.randint(0, len(contents) - 1)
        random_quote = contents[random_num].strip()

        load_dotenv()

        MY_EMAIL = os.getenv("EMAIL")
        PASSWORD = os.getenv("PASSWORD")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # add port
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Motivational Quote\n\n{random_quote}".encode("utf-8")
            )
