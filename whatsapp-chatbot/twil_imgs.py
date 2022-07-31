# receive an image from whatsapp
import os
from flask import request, Flask
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

def img_bot():
    sender = request.form.get('From')
    message = request.form.get('Body')
    media_url = request.form.get('MediaUrl0') 
    print(f'{sender} sent {media_url}')
    if media_url:
        return respond('Thank you! Your image was received.')
    else:
        return respond(f'Please send an image!')

