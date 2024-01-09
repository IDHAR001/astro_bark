import os
import requests
import schedule
import time

# Your Bark token
bark_token = os.environ.get("bark_token")

# The message to send
message = "Remember to sync the time through Astro!"

# The URL of the Bark API
bark_url = "https://api.day.app/" + bark_token + "/"

# Send a message to Bark
def send_bark_message(message):
    requests.get(bark_url + message)

# Schedule the reminder
# schedule.every(1).minutes.do(send_bark_message, message)
schedule.every().tuesday.at("1:30").do(send_bark_message, message)
schedule.every().thursday.at("1:30").do(send_bark_message, message)

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)