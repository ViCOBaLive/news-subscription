from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .SMS import SMS

    
@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

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
             response = "END You have succesfuly subsrcibed to Politics breaking news  \n"
             sms = SMS()
             sms.send(phone_number,"You have succesfuly subsrcibed to Politics breaking news")
        elif text == "1*2*1":
             response = "END You have succesfuly subsrcibed to Disasters and Accidents  \n"
        elif text == "1*3*1":
             response = "END You have succesfuly subsrcibed to Crime and Public Safety  \n"
        elif text == "2*1*1":
             response = "END You have succesfuly subsrcibed to Community Events  \n"
        elif text == "2*2*1":
             response = "END You have succesfuly subsrcibed to Education news  \n"

        elif text == "3*1*1":
             response = "END You have succesfuly subsrcibed to Stock Market news  \n"
        elif text == "3*2*1":
             response = "END You have succesfuly subsrcibed to Corporate News  \n"
        elif text == "4*1*1":
             response = "END You have succesfuly subsrcibed to Elections and Campaigns news  \n"
        elif text == "4*2*1":
             response = "END You have succesfuly subsrcibed to Government Policies and Legislation news  \n"
        elif text == "5*1*1":
             response = "END You have succesfuly subsrcibed to Medical Research and Breakthroughs news  \n"
        elif text == "5*2*1":
             response = "END You have succesfuly subsrcibed to Mental Health and Well-being news  \n"
        elif text == "6*1*1":
             response = "END You have succesfuly subsrcibed to  Football/Soccer news  \n"

        elif text == "6*2*1":
             response = "END You have succesfuly subsrcibed to Basketball sport news  \n"
        elif text == "6*3*1":
             response = "END You have succesfuly subsrcibed to Tennis/sport news  \n"
        else:
             response = "END Cancellled \n"

        return HttpResponse(response, content_type='text/plain')


