import os
import time
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

def send_sms_message():
    try:
        client = Client(account_sid, auth_token)
    except Exception as e:
        print(f"An error has occurred: {e}")


    text_message = input("Enter a message to send: ")

    recipient = input("Enter the recipient name: ")

    if recipient == 'Tim':
        cell_number = os.environ.get('CELL_PHONE_NUMBER')
    elif recipient == 'Val':
        cell_number = os.environ.get('VAL_PHONE_NUMBER')

    try:
        message = client.messages\
            .create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                                to=cell_number,
                                body=text_message)
    except Exception as e:
        print(f"An error has occurred: {e}")

    if message:
        print(f"Message sent: {message.sid}")

    else:
        print("Message not sent.")

def main():
    send_sms_message()

if __name__ == '__main__':
    main()