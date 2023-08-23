def send_sms(to, from_, body):
  # Import the Twilio API.
  import twilio
  from twilio.rest import Client

  # Your Twilio account SID and auth token.
  account_sid = "AC6b96af4ceebfef859e74bd30f48de009"
  auth_token = "db12e28e521c61de1d526f91478d6252"

  # Create a Twilio client.
  client = Client(account_sid, auth_token)

  # Send an SMS message.
  message = client.messages.create(
    to=to,
    from_=from_,
    body=body)

  print(message.sid)

# Get the admin_no.
admin_no = "123456"

# Send the SMS message.
send_sms(to="+254720051528", from_="+4706885125", body=f"Your admin_no is {admin_no}.")

# . # importing twilio

# from twilio.rest import Client

# 3. # Your Account Sid and Auth Token from twilio.com / console

# 4. account_sid = 'AC*************************************'

# 5. auth_token = '****************************************'   

# 6. client = Client(account_sid, auth_token)   

# 7. message = client.messages.create(

# 8. from_='+15017122661',

# 9. body ='body',

# 10. to ='+15558675310'

# 11. )

# 12. print(message.sid)
