import random
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'Your Account SID'
auth_token = 'Your Auth Token'
client = Client(account_sid, auth_token)
OTP = random.randint(10000, 99999)
receiver = '+959400000000'

message = client.messages \
    .create(
         body=f'Use: {OTP} for YKSA app',
         from_='+14157992342',
         to=receiver
     )

print(message.sid)
verified = input('Enter OTP: ')
if OTP == int(verified):
    print('Your account is successfully verified')
else:
    print('Wrong OTP')