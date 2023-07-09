import json
import africastalking
from django.http import HttpResponse
from django.urls import reverse
import requests
import os
# Load the .env file
import dotenv
dotenv.load_dotenv()

class SMSHandler:
    def __init__(self, get_response):
        self.get_response = get_response
        self.sender_id = os.getenv('GATEWAY_SENDER_ID')

        try:
            # Initialize the Africa's Talking API
            SANDBOX_USER = os.getenv('SANDBOX_USER')
            DEV_API_KEY = os.getenv('DEV_API_KEY')
            africastalking.initialize(username=SANDBOX_USER,api_key=DEV_API_KEY)
            self.sms = africastalking.SMS
        except Exception as e:
            print(f'Error initializing Africa\'s Talking: {str(e)}')
    def __call__(self, request):
        #get the initial endpoint url usnig django reverse
        # Check if it's an SMS-related request
        try:
            if request.method == 'POST' and request.path == reverse('send_sms'):
                data = json.loads(request.body)
                # Extract the recipients and message from the request
                recipients = data.get('recipients', [])
                message = data.get('message', '')
                

                # Send the SMS using Africa's Talking API
                response = self.send_sms(recipients, message, self.sender_id)

                # Return an appropriate HTTP response
                if response['SMSMessageData']['Recipients']:
                    #from the json response for the request 
                    res = {
                        'message': 'SMS sent successfully',
                        'data': response['SMSMessageData']['Recipients'],
                    }
                    #json encode the response
                    res = json.dumps(res)
                    return HttpResponse(res, status=200)
                else:
                    res = {
                        'status': 'error',
                        'message': 'Failed to send SMS',
                    }
                    res = json.dumps(res)
                    return HttpResponse(res, status=400)
            else:
                return self.get_response(request)
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}')

    def send_sms(self, recipients, message):
        try:
            phone = [self.normalize_phone_number(recipients)]
            #Send the SMS
            response = self.sms.send(message=message, recipients=phone, sender_id=self.sender_id)
            return response
        except Exception as e:
            # Handle any exception that occurs during sending
            print(f'Error sending SMS: {str(e)}')
            return None


    def normalize_phone_number(self,phone_number):
    # add the country code prefix if present
        if phone_number.startswith('+255'):
            phone_number = phone_number[4:]
        elif phone_number.startswith('255'):
            phone_number = phone_number[3:]
        elif phone_number.startswith('0'):
            phone_number = phone_number[1:]
        else:
            raise ValueError('Invalid phone number')

        # Add the "07" prefix to the phone number
        formatted_phone_number = '+255' + phone_number

        return formatted_phone_number
    
    def sendMultipleSMS(self, recipients, message):
            try:
                fmtd_recipients = []
                for rec in recipients:
                     phone = self.normalize_phone_number(rec)
                     fmtd_recipients.append(phone)
                print(f"Bulk recepients {fmtd_recipients}")
                #Send the SMS
                response = self.sms.send(message=message, recipients=fmtd_recipients, sender_id=self.sender_id)
                return response
            except Exception as e:
                # Handle any exception that occurs during sending
                print(f'Error sending SMS: {str(e)}')
                return None
    
# rec = ["0769642828","0769642826","0769642827","0769642829"]
# sms = SMSHandler(get_response=None)
# sms.sendMultipleSMS(rec,'News Update!  Jacoba has marrid')



