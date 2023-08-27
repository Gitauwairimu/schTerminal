import pika, sys, os, requests

def callback(ch, method, properties, body):
  print(f" [x] Received {body}")
  # Send the message to Slack
  slack_webhook_url = str(SLACK_WEBHOOK_URL)
  image_url = "https://img.freepik.com/free-photo/fashion-little-boy_71767-95.jpg?w=740&t=st=1692783130~exp=1692783730~hmac=fb5497f861438368540cc91e7c3c65af404b283a8c17fc8818a3adf18ed60042"

  payload = {
    "text": f"User {body} has been registered as {role}. Their email address is {email}",
    "username": "Registration Bot", "icon_url": image_url}
  requests.post(slack_webhook_url, json=payload)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
