import requests
from twilio.twiml.messaging_response import MessagingResponse
from flask import request


def cat_and_quote_bot():
    print(" no")
    # message from the user
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False # user will have responded if it matches any keywords. otherwise, they have not, and dummy messages can be sent
    
    # user asked for a quote by entering a quote in the message
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random') # get request
        # if successful, get the json data from the get request
        if r.status_code == 200:
            data = r.json()
            # the data provides content and author payloads -- try out different content if you want :)
            quote = f'{data["content"]}\n\t- {data["author"]}'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    # you can do multiple cases like this
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)
