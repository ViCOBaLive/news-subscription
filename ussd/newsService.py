from django.http import HttpResponse
import requests
from .SMS import send_sms

class NewsSubscriptionService:
    def __init__(self, request):
        self.request = request
        self.session_id = request.POST.get('sessionId')
        self.service_code = request.POST.get('serviceCode')
        self.phone_number = request.POST.get('phoneNumber')
        self.text = request.POST.get('text')
        self.response = ""

    def handle_request(self):
        if self.request.method == 'POST':
            if self.text == "":
                self.show_main_menu()
            elif self.text in ["1", "2", "3", "4", "5", "6"]:
                self.handle_category_selection()
            elif "*" in self.text:
                self.handle_submenu_selection()

            return HttpResponse(self.response, content_type='text/plain')

    def show_main_menu(self):
        self.response = "CON Welcome to our News subscription service \n"
        self.response += "1. Breaking News \n"
        self.response += "2. Local News \n"
        self.response += "3. Business and Finance \n"
        self.response += "4. Politics and Government \n"
        self.response += "5. Health and Wellness \n"
        self.response += "6. Sports"

    def handle_category_selection(self):
        category = int(self.text)
        if category == 1:
            self.show_submenu("Breaking News", ["Politics", "Disasters and Accidents", "Crime and Public Safety"])
        elif category == 2:
            self.show_submenu("Local News", ["Community Events", "Education"])
        elif category == 3:
            self.show_submenu("Business and Finance", ["Stock Market", "Corporate News"])
        elif category == 4:
            self.show_submenu("Politics and Government", ["Elections and Campaigns", "Government Policies and Legislation"])
        elif category == 5:
            self.show_submenu("Health and Wellness", ["Medical Research and Breakthroughs", "Mental Health and Well-being"])
        elif category == 6:
            self.show_submenu("Sports", ["Football/Soccer", "Basketball", "Tennis"])

    def show_submenu(self, category_name, subcategories):
        self.response = f"CON Select {category_name} Category \n"
        for index, subcategory in enumerate(subcategories, start=1):
            self.response += f"{index}. {subcategory} \n"

    def handle_submenu_selection(self):
        submenu = self.text.split("*")
        category = int(submenu[0])
        subcategory = int(submenu[1])

        if category == 1:
            self.confirm_subscription("Politics")
        elif category == 2:
            self.confirm_subscription("Disasters and Accidents")
        elif category == 3:
            self.confirm_subscription("Crime and Public Safety")
        elif category == 4:
            self.confirm_subscription("Community Events")
        elif category == 5:
            self.confirm_subscription("Education")
        elif category == 6:
            if subcategory == 1:
                self.confirm_subscription("Stock Market")
            elif subcategory == 2:
                self.confirm_subscription("Corporate News")
            elif subcategory == 3:
                self.confirm_subscription("Elections and Campaigns")
            elif subcategory == 4:
                self.confirm_subscription("Government Policies and Legislation")
            elif subcategory == 5:
                self.confirm_subscription("Medical Research and Breakthroughs")
            elif subcategory == 6:
                self.confirm_subscription("Mental Health and Well-being")
            elif subcategory == 7:
                self.confirm_subscription("Football/Soccer")
            elif subcategory == 8:
                self.confirm_subscription("Basketball")
            elif subcategory == 9:
                self.confirm_subscription("Tennis")

    def confirm_subscription(self, topic):
        self.response = f"CON Do you want to subscribe to {topic}? \n"
        self.response += "1. Yes \n"
        self.response += "2. No"

        test_string = self.text

        numbers = test_string.split('*')
        last_number = numbers[-1]
        if last_number == "1":
            self.send_message(f"You are now subscribed to {topic} news. Thank you!")
        elif last_number == "2":
            self.send_message(f"You have chosen not to subscribe to {topic} news. Thank you!")

    def send_message(self, message):
        try:
            send_sms(recipient_number=self.phone_number,message=message)
        except Exception as e:
            print (str(e))
        

