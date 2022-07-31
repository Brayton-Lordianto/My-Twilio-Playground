from twilio.rest import Client 
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token) 

#some code to get my number
#some code to get my number
my_number = '+1 415 523 8886'#i got my number
 
message = client.messages.create( 
                              from_='whatsapp:'+ my_number,  
                              body='message',      
                              to='whatsapp:' + '+6281510000106' ,
                          ) 
 
print(message.sid)
