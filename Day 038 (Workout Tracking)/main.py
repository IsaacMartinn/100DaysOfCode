import requests
import datetime as dt
import os 
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = 68
HEIGHT_CM = 182
AGE = 23

APP_ID = os.getenv("app_id")
API_KEY = os.getenv("api_key")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell me which exercise you did: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

paramaters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

res = requests.post(exercise_endpoint,headers=headers,json=paramaters)
result = res.json()

# duration = result['exercises'][0]["duration_min"]
# exercise_name = result['exercises'][0]['name']
# calories_burned = result['exercises'][0]['nf_calories']



#------SHEETY--------

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

SHEETY_ENDPOINT = os.getenv("sheety_endpoint")

SHEETY_TOKEN = os.getenv("sheety_token") 
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT,json=sheet_inputs,headers=sheety_headers)
    sheet_response.raise_for_status()


