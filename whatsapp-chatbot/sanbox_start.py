from twilio.rest import Client 
import os
 
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token) 
 
 
def send(sendBody):
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=sendBody,      
                                to='whatsapp:+6281510000106' 
                            ) 
    return message
 
message = send('wh aho fjefpi')
print(message.sid)