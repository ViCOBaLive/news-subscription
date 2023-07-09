import africastalking
import os
import dotenv
dotenv.load_dotenv()

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = os.getenv('SANDBOX_USER')
        self.api_key = os.getenv('DEV_API_KEY')

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

