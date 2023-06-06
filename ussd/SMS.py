import africastalking

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "sandbox"
        self.api_key = "ca3cef4bf11bf24c1d69c07ff95ff1e04b54282ad20ea7478b6dcbc93534124f"

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

