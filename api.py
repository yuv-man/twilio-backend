from flask import Flask, render_template, request
from flask_cors import CORS
from twilio.rest import Client
from flask_socketio import SocketIO, send
from decouple import config

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
app.debud = True
app.host = 'localhost'

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
app.config['SECRET_KEY'] = 'secretkey'

@app.route('/api', methods=['GET'])
def index():
    return {"status" : "Welcome welcome"}

@app.route('/api/call', methods=['POST'])
def call():
    data = request.get_json()
    phone = "+972{}".format(data["content"][1:])
    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=phone,
        from_='+15033799742',
        status_callback='http://127.0.0.1:5000',
        status_callback_event=['initiated', 'answered', 'ringing', 'completed'],
        status_callback_method='POST'
    )
    print(call.sid)
    return {"content": phone, "status": call.status } 

@socketio.on('status')
def status_change(status):
    print(status)
    send(status, broadcast=True)
    return None

@app.route('/response', methods=['POST'])
def outbound():
    status=request.values.get('CallStatus', None)
    return {"status" : status}   

if __name__ == "__main__":
    socketio.run(app)



