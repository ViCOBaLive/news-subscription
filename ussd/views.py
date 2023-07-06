import json
from ussd.middlewares import ussdMiddleware
from django.http import HttpResponse
from ussd.middlewares import IncomingSMSMiddleware
from django.views.decorators.csrf import csrf_exempt


class USSDView:
   #get  request
    @csrf_exempt
    def index(request):
        if request.method == "GET":
            data = {"message": 'You are at the USSD index'}
            data = json.dumps(data)
            return HttpResponse(data)   
    
    #post request handler
        if request.method == "POST":
            # Call the USSD middleware to handle the request and get the response
            middleware = ussdMiddleware(None)
            response = middleware(request)
            # Return the response
            return HttpResponse(response)


class IncomingSMSView:
    #get  request
    @csrf_exempt
    def index(request):
        if request.method == "GET":
            data = {"message": 'You are at the Incoming SMS index'}
            data = json.dumps(data)
            return HttpResponse(data)   
        
        #post request handler
        if request.method == "POST":
            print("Incoming SMS posted")
            # Call the USSD middleware to handle the request and get the response
            middleware = IncomingSMSMiddleware(None)
            response = middleware(request)
            # Return the response
            return HttpResponse(response)



