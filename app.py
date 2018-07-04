from flask import Flask ,url_for, request,jsonify
import json
import requests
import sys

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
def handle_requests():
    global messages

    if request.method == 'POST':
        sys.stdout.write("Message Recieved..\n\n")
        request_content = json.loads(request.get_data())
        sys.stdout.write(str(request_content))
    hdr = request.headers.get('X-Amz-Sns-Message-Type')
    if hdr== 'SubscriptionConformation' and 'SubscribeURL' in js:
        r =requests.get(js['SubscribeURL'])
        sys.stdout.write("\n\n SubscribeURL" + str(r))
        #sys.stdout.write(r)

    return "OK"

'''        # Insert newest messages to front of list
        messages.insert(0, request_content["Message"])
        return str(len(messages))

    if request.method == 'GET':
        return render_template('SNS.html', message_queue=messages)'''
'''def sns():
    try:
        js=json.loads(request.data)
    except:
        pass
    hdr = request.headers.get('X-Amz-Sns-Message-Type')

    #Sucbscribe to SNS Topic
    if hdr== 'SubscriptionConformation' and 'SubscribeURL' in js:
        r =requests.get(js['SubscribeURL'])
        sys.stdout.write(r)
        #return js

    #if hdr == 'Notification':
    #    msg_process(js['Message'],js['Timestamp'])

    return 'OK\n' '''

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port=80,
        debug=True
    )
