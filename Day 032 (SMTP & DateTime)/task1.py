import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: Hello\n\nThis is the body of my email"
    )