import keys2
from twilio.rest import Client
client=Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+13237011675"
myCellphone = '+12548787214'

textmsg=client.messages.create(to=myCellphone, from_=TwilioNumber,body='Hey there!')
print(textmsg.status)

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",to=myCellphone,from_=TwilioNumber)