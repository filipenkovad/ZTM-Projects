from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd81bf2fa7564b69beb4ba7241ed126d3'
auth_token = 'f851c450821f6eaea5f58fe32130083c'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Моё первое сообщение!",
                     from_='+16673031506',
                     to='+79119526959'
                 )

print(message.sid)