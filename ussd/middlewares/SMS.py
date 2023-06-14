import africastalking

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "sandbox"
        self.api_key = "66c5aff6bf26de8bf6176c35478f6dcef2cae57d92f24db1dd459637"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, recipient_number,reqmessage):
        # Set the number you want to send to in international format
        recipient = recipient_number

        # Set your message
        message = reqmessage

        # Set your shortCode or senderId
        sender = "SOPHY-NEWS"
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, [recipient], sender)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))

