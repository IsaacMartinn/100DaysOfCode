import requests
import datetime as dt

MY_LAT = 43.653225
MY_LONG = -79.383186

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0
}

response = requests.get('https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data = response.json() 

sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now.hour)