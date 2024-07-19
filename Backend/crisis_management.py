from twilio.rest import Client

def send_crisis_alert(phone_number, message):
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='+1234567890',  # Your Twilio phone number
        to=phone_number
    )
    return message.sid
