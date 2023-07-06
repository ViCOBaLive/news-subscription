import json
from django.http import HttpResponse
from django.urls import reverse
from news.models import Subcategory, Subscription, User
from django.core.cache import cache
from ussd.Handlers.ussdHandler import ussdHandler
from ussd.middlewares.smsMiddleware import SMSHandler
from .SMS import SMS


class IncomingSMSMiddleware:
    def __init__(self, GET_response):
        self.GET_response = GET_response

    def __call__(self, request):
        # Check if the request is a POST request and the path is /api/v1/incoming-sms/
        try:
            if request.method == 'POST' and request.path == '/incoming-sms/':
                try:
                    # chek if no data is posted an return pass the request to the next middleware
                    if not request.POST:
                        return self.GET_response(request)
                    print("Incoming SMS received")
                    # extract data from the quesry dict
                    data = request.POST

                    from_number = data['from']
                    id = data['id']
                    text = data['text']
                    to = data['to']

                    UNSUB_SHORTCODE = SUB_SHORTCODE = "49049"
                    SUB_KEYWORD = "SUB"
                    STOP_KEYWORD = "STOP"

                    if text.upper().startswith(SUB_KEYWORD) and to == SUB_SHORTCODE:
                        # Extract the subscribed services after the SUB keyword
                        subscribed_services = text[len(
                            SUB_KEYWORD):].strip().split(',')
                        MultipleSubscribe(from_number, subscribed_services)
                        return HttpResponse('Success')

                    if text.upper().startswith(STOP_KEYWORD) and to == UNSUB_SHORTCODE:
                        # Extract the subscribed services after the SUB keyword
                        unsubscribed_services = text[len(
                            STOP_KEYWORD):].strip().split(',')
                        MultipleUnsubscribe(from_number, unsubscribed_services)
                        return HttpResponse('Success')

                    error_subscription = f"Opps! failed to subscribe to the specified service , make use of correct format ie STOP XXX or SUB XXX !"
                    SMSHandler(get_response=None).send_sms(from_number, error_subscription)
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


def MultipleUnsubscribe(from_number, unsubscribed_services):
    try:
        lang = get_user_lang(from_number)
        for service in unsubscribed_services:
            Unsubscribe(lang, from_number, service)
        return True
    except Exception as e:
        print("iterate mult-unsub",str(e))
        return False

def MultipleSubscribe(from_number, subscribed_services):
    try:
        lang = get_user_lang(from_number)
        for service in subscribed_services:
            Subscribe(lang, from_number, service)
        return True
    except Exception as e:
        print("Multiple subscribe error",str(e))
        return False

  # check user preference language

#  method to unsubscribe a user from a subcategory
def Unsubscribe(lang, userphone, subcategory_name):
    try:
        user = User.objects.get(phone_number=zero_phone_number(userphone))
        subcategory = Subcategory.objects.get(name__icontains=subcategory_name)
        subscription = Subscription.objects.get(
            user=user, subcategory=subcategory)
        subscription.delete()
        print("Unsubscription successful.")
        msg = ""
        if lang == "EN":
            msg = f"You have successfully unsubcribed to {subcategory_name}, feel free to subscribe any time!"
        else:
            msg = f"Hongera, Umefanikiwa kujitoa na taarifa za {subcategory_name}, kua huru kujisajili mda wowote, asante "
        SMSHandler(get_response=None).send_sms(userphone, msg)
        return True

    except Exception as e:
        print("subscribe error",str(e))
        return False

def Subscribe(lang, userphone, subcategory_name):
    try:
        # Check if the user already exists
        user, created = User.objects.get_or_create(
            phone_number=zero_phone_number(userphone))

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
            if lang == "EN":
                msg = f"You have successfully subcribed to {subcategory_name}, feel frEE to unsubscribe any time!"
            else:
                msg = f"Hongera, Umefanikiwa kujisajili na taarifa za {subcategory_name}, kua huru kujitoa mda wowote, asante "
            SMSHandler(get_response=None).send_sms(userphone, msg)
            return True

    except Exception as e:
        print("subscribe error",str(e))
        return False


# method to get the user language preference
def get_user_lang(phone_number):
    # check if the user has a language preference if not add one and set it to engish
    user_lang_cache_key = f'{phone_number}_languagePrefs'
    language_pref = cache.get(user_lang_cache_key)

    if language_pref == None:
        # set the cache to expire after 30 days
        cache.set(user_lang_cache_key, 'EN', 2592000)
        return cache.get(user_lang_cache_key)
    else:
        return language_pref

# make sure the phone number is in the correct format
def zero_phone_number(phone_number):
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
    formatted_phone_number = '0' + phone_number

    return formatted_phone_number