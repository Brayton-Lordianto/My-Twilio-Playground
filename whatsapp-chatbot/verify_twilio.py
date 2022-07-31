# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_verification_code():
    verification = client.verify \
                     .v2 \
                     .services('VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .verifications \
                     .create(to='+15017122661', channel='whatsapp')
    return verification


def check(): 
    verification_check = client.verify \
                            .v2 \
                            .services('VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                            .verification_checks \
                            .create(to='+15017122661', code='123456')
    return verification_check

print(send_verification_code().account_sid)
print(check().status)
