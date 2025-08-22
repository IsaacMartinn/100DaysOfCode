from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Twilio credentials
ACCOUNT_SID = os.getenv("acc_sid")
AUTH_TOKEN = os.getenv("auth_token")
MY_PHONE = os.getenv("my_phone_num")



# Initialize client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send a message
message = client.messages.create(
    from_="+16893145936",   # your Twilio number
    to=MY_PHONE,      # destination number
    body="It's going to rain today"
)

# Print message info
print("Status:", message.status)
print("SID:", message.sid)
