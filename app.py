from flask import Flask ,url_for, request,jsonify
import json
import requests
import sys
import boto3
import botocore

NON_PROCESSED_INV_BUCKET= '' # replace with your bucket name
PROCESSED_INV_BUCKET =
KEY = 'docproc-invoice.txt' # replace with your object key

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World !"

@app.route("/process-invoice", methods = ['POST'])
def processInvoice():
    return " JSON Message: " + json.dumps(request.json)

@app.route("/sns-subscribe", methods=['GET','POST','PUT'])
def handle_requests():
    global messages
    '''request_content = json.loads(request.get_data())
    sys.stdout.write(str(request_content))
'''
    if request.method == 'POST':
        sys.stdout.write("\nMessage start.. \n")
        request_content = json.loads(request.get_data())
        sys.stdout.write(str(request_content))
        sys.stdout.write("\n\n Mesage End..\n\n")
        # Strange with out this print stament half Message is printed on terminal

    return "OK"

@app.route("/download")
def download():

@app.route("/upload")
def: upload():

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port=80,
        debug=True
    )
