import requests

with open(".env") as f:
  env_vars = f.read().splitlines()

SLACK_WEBHOOK_URL = env_vars[2].split("=")[1]
ACCOUNT_SID = env_vars[3].split("=")[1]
AUTH_TOKEN = env_vars[4].split("=")[1]

def send_sms(to, body):
  from twilio.rest import Client

  account_sid = ACCOUNT_SID
  auth_token = AUTH_TOKEN

  client = Client(account_sid, auth_token)

  message = client.messages.create(
    from_='+14706885125',
    body=body,
    to=to
  )


  print(message.sid)

def send_slack_message(admin_no, first_name, admin_mobile):

  # # Send a Slack message to notify the user that they have been registered.
  slack_webhook_url = str(SLACK_WEBHOOK_URL)
  image_url = "https://img.freepik.com/free-photo/fashion-little-boy_71767-95.jpg?w=740&t=st=1692783130~exp=1692783730~hmac=fb5497f861438368540cc91e7c3c65af404b283a8c17fc8818a3adf18ed60042"
  
  payload = {
    "text": f"User {first_name} has been registered.",
    "username": "Registration Bot", "icon_url": image_url}
  requests.post(slack_webhook_url, json=payload)




# ....................................................... 

# import requests, os, sys, shutil
# import psycopg2
# from contdb import connect_to_database
# from sms import send_sms
# import hashlib

# # Read the .env file: Get variablesss .
# with open(".env") as f:
#   env_vars = f.read().splitlines()

# SLACK_WEBHOOK_URL = env_vars[2].split("=")[1]


# # Send a Slack message to notify the user that they have been registered.
# slack_webhook_url = str(SLACK_WEBHOOK_URL)
# image_url = "https://img.freepik.com/free-photo/fashion-little-boy_71767-95.jpg?w=740&t=st=1692783130~exp=1692783730~hmac=fb5497f861438368540cc91e7c3c65af404b283a8c17fc8818a3adf18ed60042"

# payload = {
#   "text": f"User has been registered.",
#   "username": "Registration Bot", "icon_url": image_url}
# requests.post(slack_webhook_url, json=payload)

# ...................................


# #!/usr/bin/env python
# import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# channel.queue_declare(queue='hello')

# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='How is the going?')
# print(" [x] Sent 'Hello World!'")

# connection.close()
