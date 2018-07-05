from flask import Flask ,url_for, request,jsonify
import json
import requests
import sys


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
    sys.stdout.write(json.loads(request))

    if request.method == 'POST':
        sys.stdout.write("Message Recieved..\n\n")
        request_content = json.loads(request.get_data())
        sys.stdout.write(str(request_content))
    hdr = request.headers.get('X-Amz-Sns-Message-Type')
    if hdr== 'SubscriptionConformation' and 'SubscribeURL' in js:
        r =requests.get_data(js['SubscribeURL'])
        sys.stdout.write("\n\n SubscribeURL" + str(r))

        #sys.stdout.write(r)

    hdr = request.headers.get_data('X-Amz-Sns-Message-Type')

    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        r = request.get_data(js['SubscribeURL'])
        sys.stdout.write("SubscriptionConfirmation Received..")
        sys.stdout.write(str(r))

    else:
        sys.stdout.write(str("Notification Received..\n"))
        r=request.get_data()
        sys.stdout.write(r)

    return "OK"

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port=80,
        debug=True
    )
