from flask import Flask, request
from cat_and_quote_tutorial import *
from twil_imgs import *
from full_bot import *
from img_bot_util import *


app = Flask(__name__)

@app.route('/')
def i():
    return 'Hello World'

# you want twilio to call this post request -> of course this reminds you of using ngrok to make your localhost reachable by twilio
@app.route('/cats_quote', methods=['POST'])
def cats_quote():
    return cat_and_quote_bot()

# testing out receiving whatsapp images
@app.route('/receive_img', methods=['POST'])
def receive_img():
    return whatsapp_img_bot()
    
if __name__ == '__main__':
    app.run(port=4000)
