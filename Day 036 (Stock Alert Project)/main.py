import requests
import datetime as dt
from twilio.rest import Client 
import os 
from dotenv import load_dotenv

load_dotenv()






# mon 0 tues 1 wed 2 thurs 3 fri 4 sat 5 sun 6 

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 


stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey": STOCK_API_KEY

}
response = requests.get(f"{STOCK_ENDPOINT}",params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = data_list[0]["4. close"]
# print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100


if diff_percent < 5:
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
    #HINT 1: Think about using the Python Slice Operator

    news_parameters = {
    "q":COMPANY_NAME,
    "apiKey": NEWS_API_KEY
    }

    response_news = requests.get(f"{NEWS_ENDPOINT}",params=news_parameters)
    news_data = response_news.json()["articles"][:3]

    title_list = []
    description_list = []

    for news in news_data:
        title_list.append(news['title'])
        description_list.append(news["description"])
        TWILIO_PHONE = os.getenv("twilio_phone_num")


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number. 
    #HINT 1: Consider using a List Comprehension.
    ACCOUNT_SID = os.getenv("acc_sid")
    AUTH_TOKEN = os.getenv("auth_token")
    MY_PHONE = os.getenv("my_phone_num")

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    symbol = "🔺" if yesterday_closing_price > day_before_yesterday_closing_price else "🔻"
    print(symbol)

    # Send each article as SMS
    for i in range(3):
        print(f"Title: {title_list[i]}")
        print(f"Description: {description_list[i]}")
        message = client.messages.create(
            from_=TWILIO_PHONE,
            to=MY_PHONE,
            body=f"{STOCK}: {symbol}{round(diff_percent,2)}%\n"
                 f"Headline: {title_list[i]}\n"
                 f"Brief: {description_list[i]}\n"
        )

    