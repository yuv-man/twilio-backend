from flask import Flask, render_template, request
from flask_cors import CORS
from twilio.rest import Client

app = Flask(__name__)
CORS(app)

account_sid = 'AC8c585dcb7790bea6588a1c6e1b7f7dd5'
auth_token = '8f1fbf0277104bdb2567e3a5809a4b4e'
client = Client(account_sid, auth_token)

@app.route('/api', methods=['GET'])
def index():
    return {"status" : "Hello there"}

@app.route('/api/call', methods=['POST'])
def call():
    data = request.get_json()
    phone = "+972{}".format(data["content"][1:])
    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=phone,
        from_='+15033799742'
    )
    print(call.sid)
    return {"content": phone }    

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)