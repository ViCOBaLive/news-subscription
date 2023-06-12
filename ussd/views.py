from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .SMS import SMS

    
@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse('<h1>USSD Entry - Welcome to Sophy News</h1>')
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""
        sms = SMS()

        if text == "":
            response = "CON Welcome to our News subscription service \n"
            response += "1. Breaking News \n"
            response += "2. Local News \n"
            response += "3. Business and Finance \n"
            response += "4. Politics and Government \n"
            response += "5. Health and Wellness \n"
            response += "6. Sports"

        elif text == "1":
            response = "CON Select Breaking News Category \n"
            response += "1. Politics \n"
            response += "2. Disasters and Accidents \n"
            response += "3. Crime and Public Safety"

        elif text == "2":
            response = "CON Select Local News Category \n"
            response += "1. Community Events \n"
            response += "2. Education"

        elif text == "3":
            response = "CON Select Business and Finance Category \n"
            response += "1. Stock Market \n"
            response += "2. Corporate News"

        elif text == "4":
            response = "CON Select Politics and Government Category \n"
            response += "1. Elections and Campaigns \n"
            response += "2. Government Policies and Legislation"

        elif text == "5":
            response = "CON Select Health and Wellness Category \n"
            response += "1. Medical Research and Breakthroughs \n"
            response += "2. Mental Health and Well-being"

        elif text == "6":
            response = "CON Select Sports Category \n"
            response += "1. Football/Soccer \n"
            response += "2. Basketball \n"
            response += "3. Tennis"

        # Handling submenu validation prompts
        elif text == "1*1":
            response = "CON Do you want to subscribe to Politics? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "1*2":
            response = "CON Do you want to subscribe to Disasters and Accidents? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "1*3":
            response = "CON Do you want to subscribe to Crime and Public Safety? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "2*1":
            response = "CON Do you want to subscribe to Community Events? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "2*2":
            response = "CON Do you want to subscribe to Education? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "3*1":
            response = "CON Do you want to subscribe to Stock Market? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "3*2":
            response = "CON Do you want to subscribe to Corporate News? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "4*1":
            response = "CON Do you want to subscribe to Elections and Campaigns? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "4*2":
            response = "CON Do you want to subscribe to Government Policies and Legislation? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "5*1":
            response = "CON Do you want to subscribe to Medical Research and Breakthroughs? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "5*2":
            response = "CON Do you want to subscribe to Mental Health and Well-being? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "6*1":
            response = "CON Do you want to subscribe to Football/Soccer? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "6*2":
            response = "CON Do you want to subscribe to Basketball? \n"
            response += "1. Yes \n"
            response += "2. No"

        elif text == "6*3":
            response = "CON Do you want to subscribe to Tennis? \n"
            response += "1. Yes \n"
            response += "2. No"

        # confirmationn menus 
        elif text == "1*1*1":
             response = "END You have succesfuly subscribed to Politics breaking news  \n"
             print('sending sms')
             sms.send(phone_number,"You have succesfuly subscribed to Politics breaking news")
        elif text == "1*2*1":
             response = "END You have succesfuly subscribed to Disasters and Accidents  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Disasters and Accidents ")

        elif text == "1*3*1":
             response = "END You have succesfuly subscribed to Crime and Public Safety  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Crime and Public Safety ")

        elif text == "2*1*1":
             response = "END You have succesfuly subscribed to Community Events  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Community Events ")

        elif text == "2*2*1":
             response = "END You have succesfuly subscribed to Education news  \n"
             sms.send(phone_number," You have succesfuly subscribed to Education news ")


        elif text == "3*1*1":
             response = "END You have succesfuly subscribed to Stock Market news  \n"
             sms.send(phone_number," You have succesfuly subscribed to Stock Market news ")

        elif text == "3*2*1":
             response = "END You have succesfuly subscribed to Corporate News  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Corporate News")

        elif text == "4*1*1":
             response = "END You have succesfuly subscribed to Elections and Campaigns news  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Elections and Campaigns news")

        elif text == "4*2*1":
             response = "END You have succesfuly subscribed to Government Policies and Legislation news  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Government Policies and Legislation news")

        elif text == "5*1*1":
             response = "END You have succesfuly subscribed to Medical Research and Breakthroughs news  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Medical Research and Breakthroughs news")

        elif text == "5*2*1":
             response = "END You have succesfuly subscribed to Mental Health and Well-being news  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Mental Health and Well-being news")

        elif text == "6*1*1":
             response = "END You have succesfuly subscribed to  Football/Soccer news  \n"
             sms.send(phone_number,"You have succesfuly subscribed to  Football/Soccer news")


        elif text == "6*2*1":
             response = "END You have succesfuly subscribed to Basketball sport news  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Basketball sport news")

        elif text == "6*3*1":
             response = "END You have succesfuly subscribed to Tennis/sport news  \n"
             sms.send(phone_number,"You have succesfuly subscribed to Tennis/sport news")

        else:
             response = "END Cancellled \n"
             sms.send(phone_number,"Thank you for using SOPHY NEWS, Please try again later")


        return HttpResponse(response, content_type='text/plain')



@csrf_exempt
def incomingSMS(request):
    if request.method == "GET":
         return HttpResponse("<h1>Incoming SMS Entry Point</h1>")

    if request.method == 'POST':
                    print("Incoming SMS now")
                    # extract data from the quesry dict
                    data = request.POST

                    from_number = data['from']
                    id = data['id']
                    link_id = data['linkId']
                    text = data['text']
                    to = data['to']
                    
                    SUB_KEYWORD = "SUB"
                    sms = SMS()


                    if text.upper().startswith(SUB_KEYWORD) and to == "3445":
                        # Extract the subscribed services after the SUB keyword
                        subscribed_services = text[len(SUB_KEYWORD):].strip().split(',')
                        
                        # Generate the subscription message with the list of subscribed services
                        subscription_message = "You have successfully subscribed to {}. You will receive news once available".format(", ".join(subscribed_services))
                        
                        # Send the subscription SMS
                        sms.send(from_number, subscription_message)
                        return HttpResponse('Success')
                    
                    STOP_KEYWORD = "STOP"
                    
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




                    


