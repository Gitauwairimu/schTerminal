with open(".env") as f:
  env_vars = f.read().splitlines()

ACCOUNT_SID = env_vars[3].split("=")[1]
AUTH_TOKEN = env_vars[4].split("=")[1]

def send_sms():
# def send_sms(to, body):
  from twilio.rest import Client

  # account_sid = 'AC6b96af4ceebfef859e74bd30f48de009'
  # auth_token = '83c48141f5dfb7cbbe1d74898e5c7620'

  account_sid = ACCOUNT_SID
  auth_token = AUTH_TOKEN

  client = Client(account_sid, auth_token)

  # admin_no = 1234
  # body = f"Your admin_no is {admin_no}.")
  # body = f"Your admin_no is {admin_no}"
  body = f"Thank you"

  # message = client.messages.create(
  #   from_='+14706885125',
  #   body=body,
  #   to=to
  # )


  message = client.messages.create(
    from_='+14706885125',
    body=body,
    to='+254720051528'
  )

  print(message.sid)