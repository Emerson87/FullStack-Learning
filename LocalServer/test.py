from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "AC40ec3ca6fd7ee0558c35ebebe6c8a290" # Your Account SID from www.twilio.com/console
auth_token  = "a3503a1f1e96c15e524547c36f6b9382"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(body="Paula Te amo mto, minha esposa amada e carinha de ratinha linda",
        to="+5592981002555",    # Replace with your phone number
        from_="+12345678901") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
