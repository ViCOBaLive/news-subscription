from django.core.cache import cache


def changelanguage(self):
    #check if the user has a language preference if not add one and set it to engish
    lang = 'EN' if self.lang == "SW" else "SW"
    try:
        user_lang_cache_key = f'{self.phone_number}_languagePrefs'
        cache.set(user_lang_cache_key, lang, 2592000)
        return self.response.languageChangeSuccess()
    except:
        return self.response.languageChangeError()
