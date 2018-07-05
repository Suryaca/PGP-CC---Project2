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
    '''request_content = json.loads(request.get_data())
    sys.stdout.write(str(request_content))
'''
    if request.method == 'POST':
        sys.stdout.write("\n\n\Message Recieved\n\n")
        request_content = json.loads(request.get_data())
        sys.stdout.write(str(request_content))
        #json.loads(request_content['Message'])
        sys.stdout.write(str(request_content[s3][object]))
        x = json.loads(request_content['Message'])
        sys.stdout.write("\n\n Notification Recieved\n\n")
        sys.stdout.write(str(x))
        return "OK"

'''@app.route("/sns", methods=['GET','POST','PUT'])
def sns():

    try:
        js = json.loads(request.data)
    except:
        pass

    hdr = request.headers.get('X-Amz-Sns-Message-Type')
    # subscribe to the SNS topic
    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        r = requests.get(js['SubscribeURL'])
        sys.stdout.write("Message Recieved")
        sys.stdout.write(str(r))

    if hdr == 'Notification':
        #msg_process(js['Message'], js['Timestamp'])
        #sys.stdout.write("Notification Recieved")
        sys.stdout.write(hdr)

    return 'OK\n'
'''

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port=80,
        debug=True
    )
