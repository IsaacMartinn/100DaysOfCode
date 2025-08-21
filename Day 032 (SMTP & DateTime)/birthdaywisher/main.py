
import datetime as dt
import pandas
import random
import smtplib
from dotenv import load_dotenv
import os


now = dt.datetime.now()

data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")

for i in birthday_dict:
    if i['month'] == now.month and i['day'] == now.day:
        random_num = str(random.randint(1,3))
        
        with open(f"./letter_templates/letter_{random_num}.txt") as file: 
            contents = file.read()
            new_letter = contents.replace("[NAME]",i["name"])
            # print(new_letter)
        
        load_dotenv()

        MY_EMAIL = os.getenv("EMAIL")
        PASSWORD = os.getenv("PASSWORD")

        with smtplib.SMTP("smtp.gmail.com") as connection:  
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Happy Birthday!\n\n{new_letter}".encode("utf-8")
            )
