'''
GET: to give data to the swift program, just do json.dumps
POST: to get json data, use get json to get the json data
'''
from flask import Flask, request
from ckdb_g import *
import json

app = Flask(__name__)

@app.route('/')
def i():
    return 'Hello World'

@app.route('/get_testdata')
def getdata():
    res = get_items()
    print("hi", json.dumps(res))
    return json.dumps(res)

@app.route('/test_post', methods=['POST'])
def test_post():
    payload = request.get_json()
    info, data = payload['info'], payload['data']
    print(info)
    print(data)
    print(type(request.get_json()) is list)
    print(type(request.get_json()) is dict)
    return json.dumps(get_items())
    
@app.route('/add_data', methods=['POST'])
def add_data():
    payload = request.get_json()
    # if type(doc) is list: upsert_many()
    return 'Hello'


    
if __name__ == '__main__':
    app.run(port=4000)
