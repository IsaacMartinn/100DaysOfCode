import requests
from twilio.rest import Client 
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("api_key")

URL ="https://api.openweathermap.org/data/2.5/forecast"
LAT = os.getenv("latitude") 
LONG = os.getenv("longitude")
ACCOUNT_SID = os.getenv("acc_sid")
AUTH_TOKEN = os.getenv("auth_token")

paramaters = {
    "lat": LAT,
    "lon":LONG,
    "appid":API_KEY
}

response = requests.get(url=URL,params=paramaters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data['list'][0]['weather'][0]['id'])

will_rain = False

for hour_data in weather_data["list"][:4]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) >= 700:
        will_rain = True
if will_rain: 

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_="+16893145936",   
        to=os.getenv("my_phone_num"),      
        body="It's going to rain todayxdxd"
    )
    print("Status:", message.status)
    print("SID:", message.sid)

