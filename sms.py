import os
# with open(".env") as f:
#   env_vars = f.read().splitlines()

# ACCOUNT_SID = env_vars[3].split("=")[1]
# AUTH_TOKEN = env_vars[4].split("=")[1]


def send_sms(to, body):
  from twilio.rest import Client

  account_sid = os.getenv("ACCOUNT_SID")
  auth_token = os.getenv("AUTH_TOKEN")

  # account_sid = ACCOUNT_SID
  # auth_token = AUTH_TOKEN

  client = Client(account_sid, auth_token)

  message = client.messages.create(
    from_='+14706885125',
    body=body,
    to=to
  )

  print(message.sid)
