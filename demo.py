import os
import requests
import schedule
import time

# Your Bark token
lingjie_bark_token = os.environ.get("lingjie_bark_token")
jacob_bark_token = os.environ.get("jacob_bark_token")


# The message to send
message = "布置给家长要买的辅导书^^"

# The URL of the Bark API
bark_url = "https://api.day.app/" + lingjie_bark_token + "/"

# Send a message to Bark
def send_bark_message(message):
    requests.get(bark_url + message)

schedule.every().thursday.at("05:30").do(send_bark_message, message)

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)