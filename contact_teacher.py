from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


def send_email(to_email, subject, body, sender_email, password):
  """Sends an email to the specified email address."""

  # Create the email message.
  message = MIMEMultipart()
  message["from"] = "Chao"
  message["to"] = to_email
  message["subject"] = subject
  message.attach(MIMEText(body))

  # Send the email message.
  with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, password)
    # smtp.login("gitauwairimu@gmail.com", "wflsabowleezvagw")
    smtp.send_message(message)
    print("Sent...")


# if __name__ == "__main__":
#   to_email = input("Enter the teachers's email address: ")
#   subject = input("Enter the subject: ")
#   body = input("Enter the body of the email: ")
#   print('Sending Email: Wait for Confirmation')
#   send_email(to_email, subject, body)
