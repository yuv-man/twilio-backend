from twilio.rest import Client

account_sid = 'AC8c585dcb7790bea6588a1c6e1b7f7dd5'
auth_token = '8f1fbf0277104bdb2567e3a5809a4b4e'
client = Client(account_sid, auth_token)

call = client.calls.create(
    twiml= <Response><Say>hello world</Say></Response>,
    to=
)