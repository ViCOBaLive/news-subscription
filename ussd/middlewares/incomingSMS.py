import json
from django.http import HttpResponse
from django.urls import reverse
from .SMS import SMS

class IncomingSMSMiddleware:
    def __init__(self, GET_response):
        self.GET_response = GET_response

    def __call__(self, request):
        # Check if the request is a POST request and the path is /api/v1/incoming-sms/
        try:
            if request.method == 'POST' and request.path == '/incoming-sms/':
                # print(request.POST)
                try:
                    # chek if no data is posted an return pass the request to the next middleware
                    if not request.POST:
                        return self.GET_response(request)
                    print("Incoming SMS")
                    # extract data from the quesry dict
                    data = request.POST

                    from_number = data['from']
                    id = data['id']
                    link_id = data['linkId']
                    text = data['text']
                    to = data['to']

                    
                    BASE_URL = request.build_absolute_uri(reverse('api_index'))

                    SUB_SHORTCODE = "60060"
                    SUB_KEYWORD = "SUB"
                    STOP_KEYWORD = "STOP"
                    sms = SMS()


                    if text.upper().startswith(SUB_KEYWORD) and to == SUB_SHORTCODE:
                        # Extract the subscribed services after the SUB keyword
                        subscribed_services = text[len(SUB_KEYWORD):].strip().split(',')
                        
                        # Generate the subscription message with the list of subscribed services
                        subscription_message = "You have successfully subscribed to {}. You will receive news once available".format(", ".join(subscribed_services))
                        
                        # Send the subscription SMS
                        sms.send(from_number, subscription_message)
                        return HttpResponse('Success')
                    
                    
                    if text.upper().startswith(STOP_KEYWORD) and to == "3445":
                        # Extract the subscribed services after the SUB keyword
                        unsubscribed_services = text[len(STOP_KEYWORD):].strip().split(',')
                        
                        # Generate the subscription message with the list of subscribed services
                        subscription_message = "You have unsubscribed to {} News. feel free to re-subscribe again soon ".format(",".join(unsubscribed_services))
                        
                        # Send the subscription SMS
                        sms.send(from_number, subscription_message)
                        return HttpResponse('Success')
                    
                    error_subscription = f"Opps! failed to subscribe to the specified service , make use of correct format ie STOP XXX or SUB XXX !"
                    sms.send(from_number, error_subscription)
                    return HttpResponse('Failed !')
                except Exception as e:
                    # print(e)
                    return self.GET_response(request)

            # Pass the request to the next middleware
            response = self.GET_response(request)
            return response
        except Exception as e:
            print(e)
            return self.GET_response(request)
