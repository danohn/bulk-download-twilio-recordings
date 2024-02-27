import os
from twilio.rest import Client
import requests
from dotenv import load_dotenv
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S"
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

start_time = time.time()

load_dotenv()

logger.info("Creating recordings directory")
os.makedirs("recordings", exist_ok=True)

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

if not account_sid or not auth_token:
    logger.error("Please provide valid Twilio credentials.")
    exit()

client = Client(account_sid, auth_token)

BASE_MEDIA_URL = f"http://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings"

recording_list = []

try:
    logger.info("Retreiving list of recordings")
    recordings = client.recordings.list()
except Exception as e:
    logger.error(f"Error retrieving recordings: {str(e)}")
    exit()

logger.info("Saving recordings to a List")
for record in recordings:
    media_url = f"{BASE_MEDIA_URL}/{record.sid}"
    recording_list.append(media_url)

    try:
        r = requests.get(media_url, auth=(account_sid, auth_token))
        r.raise_for_status()
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Failed to download {record.sid}: {str(req_err)}")
        continue

    with open(f"recordings/{record.sid}.wav", "wb") as f:
        f.write(r.content)
        logger.info(f"{record.sid} saved successfully")

end_time = time.time()
execution_time = round(end_time - start_time, 2)

logger.info(f"It took {execution_time} seconds to download all recordings")
