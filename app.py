import os
from twilio.rest import Client
import requests
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

if not account_sid or not auth_token:
    print("Please provide valid Twilio credentials.")
    exit()

client = Client(account_sid, auth_token)

BASE_MEDIA_URL = f"http://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings"

try:
    recordings = client.recordings.list()
except Exception as e:
    print(f"Error retrieving recordings: {str(e)}")
    exit()

for record in recordings:
    media_url = f"{BASE_MEDIA_URL}/{record.sid}"
    print(f"About to download Recording {record.sid}")

    try:
        r = requests.get(media_url, auth=(account_sid, auth_token))
        r.raise_for_status()
    except requests.exceptions.RequestException as req_err:
        print(f"Error downloading media for {record.sid}: {str(req_err)}")
        continue

    with open(f"recordings/{record.sid}.wav", "wb") as f:
        f.write(r.content)
        print(f"{record.sid} saved successfully")
