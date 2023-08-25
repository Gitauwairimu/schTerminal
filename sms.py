# def send_sms(to, from_, body):
#   # Import the Twilio API.
#   import twilio
#   from twilio.rest import Client

#   # Your Twilio account SID and auth token.
#   account_sid = "AC6b96af4ceebfef859e74bd30f48de009"
#   auth_token = "db12e28e521c61de1d526f91478d6252"

#   # Create a Twilio client.
#   client = Client(account_sid, auth_token)

#   # Send an SMS message.
#   message = client.messages.create(
#     to=to,
#     from_=from_,
#     body=body)

#   print(message.sid)

# # Get the admin_no.
# admin_no = "123456"

# # Send the SMS message.
# send_sms(to="+254720051528", from_="+14706885125", body=f"Your admin_no is {admin_no}.")


# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

account_sid = 'AC6b96af4ceebfef859e74bd30f48de009'
auth_token = '83c48141f5dfb7cbbe1d74898e5c7620'
client = Client(account_sid, auth_token)

admin_no = 1234
# body = f"Your admin_no is {admin_no}.")
body = f"Your admin_no is {admin_no}"


message = client.messages.create(
  from_='+14706885125',
  body=body,
  to='+254720051528'
)

print(message.sid)