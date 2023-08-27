with open(".env") as f:
  env_vars = f.read().splitlines()

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

admin_mobile="+254720051528"
send_sms(to=admin_mobile, body="Welcome, Use admin number: 1 to login. Account created.")