from flask import Flask ,url_for, request,jsonify
import json
import requests
import sys

'''def msg_process(msg, tstamp):
    js = json.loads(msg)
    sys.stdout.write(str(js))
    message = event[‘Records’][0][‘Sns’][‘Message’]
    print(“From SNS: “ + message)
    return message'''

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

    if request.method == 'POST':
        sys.stdout.write("Message Recieved..\n\n")
        request_content = json.loads(request.get_data())
        sys.stdout.write(str(request_content))

    hdr = request.headers.get_data('X-Amz-Sns-Message-Type')

    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        r = requests.get_data(js['SubscribeURL'])
        sys.stdout.write("SubscriptionConfirmation Received..")
        sys.stdout.write(str(r))

    else
        sys.stdout.write(str("Notification Received..\n"))
        #msg_process()
        message = event[‘Records’][0][‘Sns’][‘Message’]
        print(“From SNS: “ + message)

    return "OK"

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port=80,
        debug=True
    )
