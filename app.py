from flask import Flask ,url_for, request,jsonify
import json
import requests

def msg_process(msg, tstamp):
    js = json.loads(msg)
    msg = 'Region: {0} / Alarm: {1}'.format(
        js['Region'], js['AlarmName']
    )

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World !"

@app.route("/process-invoice", methods = ['POST'])
def processInvoice():
    return " JSON Message: " + json.dumps(request.json)

@app.route("/sns-subscribe", methods=['GET','POST','PUT'])
def sns():
    try:
        js=json.loads(request.data)
    except:
        pass
    hdr = request.headers.get('X-Amz-Sns-Message-Type')

    #Sucbscribe to SNS Topic
    if hdr== 'SubscriptionConformation' and 'SubscribeURL' in js:
        r =requests.get(js['SubscribeURL'])

    return js

    #if hdr == 'Notification':
    #    msg_process(js['Message'],js['Timestamp'])

    #return 'OK\n'

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port=80,
        debug=True
    )
