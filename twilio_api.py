from twilio.rest import Client
import requests

# Script that gets data from an API endpoint and formulates a message and sends an SMS 

# API access credentials
account_sid = 'AC6eb198559bdf529bdcd2ef3d93a843ef'
auth_token = '457308d9fb345baee370d1ad0b703f41'

client = Client(account_sid, auth_token)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

number_iss = people['number']
Message = 'Hi Fun fact,Number of people in space right now is '+str(number_iss)

# Formulate the message that will be sent
message = client.messages.create(
    to="+16044464331",
    from_="+12058517943",
    body=Message)
print(message.sid)