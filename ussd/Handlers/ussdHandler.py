import json
import requests
from ussd.Menus import Registered, ussdResponses
from ussd.Handlers.utils import langs
from django.core.cache import cache
from news.models import User, Subscription, Subcategory
from ussd.middlewares.smsMiddleware import SMSHandler
from django.db.models import Q


class ussdHandler():
    def __init__(self, text, session_id, phone_number, lang, base_url, request):
        self.text = text
        self.phone_number = phone_number
        self.request = request
        self.lang = lang
        self.base_url = base_url
        self.menu = Registered.RegisteredMenu(
            self.lang, self.base_url, self.phone_number, self.request)
        self.response = ussdResponses.USSDResponseHandler(self.lang)
        self.cache = cache
        self.sms = SMSHandler(get_response=None)

    def handler(self):
        # split the text
        textArray = self.text.split('*')
        # check the ussd level
        level = len(textArray)

        if self.text == '':
            return self.menu.MainMenu('Sophy News')

        if level == 1:
            if textArray[0] == '1':
                print('politics menus')
                return self.menu.PoliticsMenu()
            # health menus
            elif textArray[0] == '2':
                return self.menu.HealthMenu()
            # sports services menus
            elif textArray[0] == '3':
                return self.menu.SportsMenu()
            # business menus
            elif textArray[0] == '4':
                return self.menu.BusinessMenu()
            # change language
            elif textArray[0] == '5':
                return langs.changelanguage(self)
            elif textArray[0] == '6':
                return self.menu.unsubscribeMenu()
            else:
                return self.response.invalid_input()
        if level == 2:
            msge = ""
            # politics
            if textArray[0] == '1' and textArray[1] == '1':
                msg = 'Domestic Politics' if self.lang == "EN" else "Siasa za nyumbani"
                return self.menu.ApprovalMenu(msg)
            if textArray[0] == '1' and textArray[1] == '2':
                msg = 'Internationsl Politics' if self.lang == "EN" else "Siasa za nje"
                return self.menu.ApprovalMenu(msg)
            # health
            if textArray[0] == '2' and textArray[1] == '1':
                msg = 'Self Health Tips' if self.lang == "EN" else "Dodoso za Afya"
                return self.menu.ApprovalMenu(msg)
            if textArray[0] == '2' and textArray[1] == '2':
                msg = 'Food and Diet' if self.lang == "EN" else "Chakula na Afya ya Chakula"
                return self.menu.ApprovalMenu(msg)
            # sports
            if textArray[0] == '3' and textArray[1] == '1':
                msg = 'Domestic Sports' if self.lang == "EN" else "Michezo ya Ndani"
                return self.menu.ApprovalMenu(msg)
            if textArray[0] == '3' and textArray[1] == '2':
                msg = 'International Sports' if self.lang == "EN" else "Michezo ya Nje"
                return self.menu.ApprovalMenu(msg)
            # business
            if textArray[0] == '4' and textArray[1] == '1':
                msg = 'Stock Market' if self.lang == "EN" else "Soko La Hisa"
                return self.menu.ApprovalMenu(msg)
            if textArray[0] == '4' and textArray[1] == '2':
                msg = 'Currency Exchange Rates' if self.lang == "EN" else "Thamani ya Fedha za Kigeni"
                return self.menu.ApprovalMenu(msg)
            if textArray[0] == '4' and textArray[1] == '3':
                msg = 'Daily Business Tips' if self.lang == "EN" else "Dodoso za Biashara / Kila siku"
                return self.menu.ApprovalMenu(msg)
            # unsubscribe
            if textArray[0] == '6' and textArray[1] is not None and textArray[1].isnumeric():
                return self.menu.unsubscribeConfirm(textArray[1])
        # approval
        if level == 3:
            if self.text == "1*1*1":
                print('subscribing to domestic politics news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='DOMESTIC POLITICS'):
                    return self.menu.SubSucccesfullRes('politics')
                else:
                    return self.menu.SubFailedRes()
            if self.text == "1*2*1":
                print('subscribing to INTERNATIONAL POLITICS news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='INTERNATIONAL POLITICS'):
                    return self.menu.SubSucccesfullRes('INTERNATIONAL POLITICS ')
                else:
                    return self.menu.SubFailedRes()
            if self.text == "2*1*1":
                print('subscribing to COVID-19  news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='SELF CARE'):
                    return self.menu.SubSucccesfullRes('SELF CARE')
                else:
                    return self.menu.SubFailedRes()
            if self.text == "2*2*1":
                print('subscribing to FOOD AND DIET news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='FOOD AND DIET'):
                    return self.menu.SubSucccesfullRes('FOOD AND DIET')
                else:
                    return self.menu.SubFailedRes()

            if self.text == "3*1*1":
                print('subscribing to domestic sports news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='DOMESTIC SPORTS'):
                    return self.menu.SubSucccesfullRes('DOMESTIC SPORTS')
                else:
                    return self.menu.SubFailedRes()
            if self.text == "3*2*1":
                print('subscribing to international sports news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='INTERNATIONAL SPORTS'):
                    return self.menu.SubSucccesfullRes('INTERNATIONAL SPORTS')
                else:
                    return self.menu.SubFailedRes()
            if self.text == "4*1*1":
                print('subscribing to stock market news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='STOCK MARKET'):
                    return self.menu.SubSucccesfullRes('STOCK MARKET')
                else:
                    return self.menu.SubFailedRes()
            if self.text == "4*2*1":
                print('subscribing to currency exchange news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='CURRENCY EXCHANGE'):
                    return self.menu.SubSucccesfullRes('CURRENCY EXCHANGE')
                else:
                    return self.menu.SubFailedRes()
            if self.text == "4*3*1":
                print('subscribing to business advice news')
                if self.Subscribe(userphone=self.phone_number, subcategory_name='BUSINESS TIPS'):
                    return self.menu.SubSucccesfullRes('BUSINESS TIPS')
                else:
                    return self.menu.SubFailedRes()
            if textArray[0] == '6' and self.is_within_range(textArray[1]) and textArray[2] == '1':
                news_cat = self.menu.mapNumtoProduct(textArray[1])
                unsub = self.Unsubscribe(
                    userphone=self.phone_number, subcategory_name=news_cat)
                if unsub:
                    return self.menu.unSubscribeSuccess(textArray[1])
                else:
                    return self.menu.unSubscribeFailed()
            else:
                print("Invalid input")

    def Subscribe(self, userphone, subcategory_name):
        try:
            # Check if the user already exists
            user, created = User.objects.get_or_create(phone_number=userphone)

            if created:
                # User was created, set the password
                user.set_password("pass")
                user.save()

            subcategory = Subcategory.objects.get(
                name__icontains=subcategory_name)
            # Check if the user is already subscribed to the subcategory
            subscription, subscription_created = Subscription.objects.get_or_create(
                user=user, subcategory=subcategory)

            if not subscription_created:
                print("User is already subscribed to this subcategory.")
                return True

            # Perform any additional subscription-related operations here
            if subscription:
                print("Subscription successful.")
                msg = ""
                if self.lang == "EN":
                    msg = f"You have successfully subcribed to {subcategory_name}, feel frEE to unsubscribe any time!"
                else:
                    msg = f"Hongera, Umefanikiwa kujisajili na taarifa za {subcategory_name}, kua huru kujitoa mda wowote, asante "
                self.sms.send_sms(self.phone_number, msg)
                return True

        except Exception as e:
            print(str(e))
            return False

    def Unsubscribe(self, userphone, subcategory_name):
        print('Unsubscribing to ' + subcategory_name + ' news')
        if subcategory_name == 'All':
            # delete all subscriptions for this user
            user = User.objects.get(phone_number=userphone)
            subscriptions = Subscription.objects.filter(user=user)
            for subscription in subscriptions:
                subscription.delete()
            print("Unsubscription to all successful.")
            msg = ""
            if self.lang == "EN":
                msg = f"You have successfully unsubscribed from all news. Feel free to subscribe again anytime!"
            else:
                msg = f"Hongera! Umefanikiwa kujitoa kwenye taarifa zote. Karibu kusajili tena wakati wowote!"
            self.sms.send_sms(self.phone_number, msg)

            return True
        try:
            # Check if the user already exists
            user = User.objects.get(phone_number=userphone)

            # Construct the query using Q objects
            query = Q(user=user) & Q(
                subcategory__name__icontains=subcategory_name)

            # Check if the subscription exists
            subscription = Subscription.objects.filter(query).first()
            print(subscription)

            if subscription:
                print("Unsubscription successful.")
                msg = ""
                if self.lang == "EN":
                    msg = f"You have successfully unsubscribed from {subscription.subcategory.name} news. Feel free to subscribe again anytime!"
                else:
                    msg = f"Hongera! Umefanikiwa kujitoa kwenye taarifa za {subscription.subcategory.name}. Karibu kusajili tena wakati wowote!"
                self.sms.send_sms(self.phone_number, msg)
                subscription.delete()
                return True
            else:
                # Subscription does not exist
                return False

        except User.DoesNotExist:
            # User does not exist
            return False
        except Exception as e:
            print(str(e))
            return False

    def is_within_range(self, value):
        if value.isnumeric():
            numeric_value = int(value)
            return numeric_value >= 1 and numeric_value <= 10 or numeric_value == 98 or numeric_value == 99
        else:
            return False
