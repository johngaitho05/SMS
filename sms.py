import africastalking

# Authentication variables
username="app-name"
api_key="your api-key"
# Creating an instance of africastalking

africastalking.initialize(username,api_key)
sms= africastalking.SMS

# send an SMS
response= sms.send("Your message", ['phone-number'])

# Logging into the console
print(response)
