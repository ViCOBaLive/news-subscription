from django.http import HttpResponse
from django.urls import reverse
import requests
from ussd.Handlers import ussdHandler
from django.core.cache import cache
from django.utils import timezone


def normalize_phone_number(phone_number):
    # Remove the country code prefix if present
    if phone_number.startswith('+255'):
        phone_number = phone_number[4:]
    elif phone_number.startswith('255'):
        phone_number = phone_number[3:]
    elif phone_number.startswith('0'):
        phone_number = phone_number[1:]
    else:
        raise ValueError(' Invalid phone number')

    # Add the "07" prefix to the phone number
    formatted_phone_number = '07' + phone_number[1:]

    return formatted_phone_number


class ussdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #get the initial endpoint url usnig django reverse
        initial_endpoint = reverse('index')
        #build ana absolute url based on the inital endpoint for the request object to be used in the ussd handler
        BASE_URL = request.build_absolute_uri(initial_endpoint)
        try:
            if request.method == 'POST':
                #request supplied by the user
                # Get the parameters from the request
                session_id = request.POST.get('sessionId')
                phone_number = request.POST.get('phoneNumber')
                text = request.POST.get('text')

                # check if the parameteres are empty and return the initial response
                if session_id == None or phone_number == None or text == None:
                    return self.get_response(request)

                # normalize the phonenumber
                try:
                    # Normalize the phone number
                    phone_number = normalize_phone_number(phone_number)
                except ValueError as e:
                    # Return an error response if the phone number is invalid
                    response = HttpResponse(f'Error: {str(e)}')
                    response['Content-Type'] = 'text/plain'
                    #cors headers
                    response['Access-Control-Allow-Origin'] = '*'
                    return response

                # check if the user has a language preference if not add one and set it to engish
                lang = self.get_user_lang(phone_number)
                
                # normalize the text for go back or main menu inputs
                text = self.go_Back(self.goToMainMenu(text))
                
                Handler = ussdHandler(
                        text, session_id, phone_number, lang, BASE_URL,request).handler()
                # Return the response with content type set to text/html
                response = HttpResponse(Handler)
                response['Content-Type'] = 'text/plain'

                if Handler == None:
                    response['Content-Type'] = 'text/plain'
                    response.content = 'END Invalid input,Please try again.'
                    return response
                return response
            return self.get_response(request)
        except Exception as e:
            response = f'Error: {str(e)}'
            return response

    # check user preference language
    def get_user_lang(self, phone_number):
        # check if the user has a language preference if not add one and set it to engish
        user_lang_cache_key = f'{phone_number}_languagePrefs'
        language_pref = cache.get(user_lang_cache_key)

        if language_pref == None:
            # set the cache to expire after 30 days
            cache.set(user_lang_cache_key, 'EN', 2592000)
            return cache.get(user_lang_cache_key)
        else:
            return language_pref

      

    def go_Back(self, text):
        textArray = text.split("*")
        while "98" in textArray:
            # Find the index of the next occurrence of the "go back" token.
            startIndex = textArray.index("98")
            # Remove the two textArray at the index of the "go back" token.
            textArray.pop(startIndex)
            textArray.pop(startIndex - 1)
        # Join the textArray back together into a string.
        return ("*".join(textArray))

    def goToMainMenu(self, text):
        explodedText = text.split("*")
        while "99" in explodedText:
            firstIndex = explodedText.index("99")
            explodedText = explodedText[firstIndex + 1:]
        return ("*".join(explodedText))
