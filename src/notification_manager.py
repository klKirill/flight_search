import smtplib
from twilio.rest import Client

TWILIO_SID = 'SID'
TWILIO_AUTH_TOKEN = 'auth token'
TWILIO_VIRTUAL_NUMBER = 'virtual number'
TWILIO_VERIFIED_NUMBER = 'verified number'
MAIL_PROVIDER_SMTP_ADDRESS = 'email smtp address'
MY_EMAIL = 'адрес почты'
MY_PASSWORD = 'пароль'

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )