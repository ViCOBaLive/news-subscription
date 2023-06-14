class USSDResponseHandler:
    def __init__(self, lang):
        self.lang = lang

    def get_response(self, text):
        return f"END {text} \n"
    

    def invalid_input(self):
        if self.lang == 'EN':
            error = "Invalid input or choice, Please try again !\n"
            return self.get_response(error)
        elif self.lang == 'SW':
            error = "Uingizaji usio sahihi, Tafadhali jaribu tena !\n"
            return self.get_response(error)

    def Success(self):
        if self.lang == 'EN':
            message = " Success"
            return self.get_response(message)
        elif self.lang == 'SW':
            message = "Imefanikiwa"
            return self.get_response(message)

    def Error(self):
        if self.lang == 'EN':
            error = self.get_response("Error")
            return error
        elif self.lang == 'SW':
            error = self.get_response(" Imekosewa")
            return error

    def cancelRequestResponse(self):
        if self.lang == 'EN':
            return self.get_response('Your request has been cancelled , You may try again later.')

        elif self.lang == 'SW':
            return self.get_response('Ombi lako limesitishwa, Unaweza kujaribu tena baadae.')

    def requestBeingprocessed(self):
        if self.lang == 'EN':
            return self.get_response('Your request is being processed, You will receive a confirmation message shortly.')

        elif self.lang == 'SW':
            return self.get_response('Ombi lako linashughulikiwa, Utapokea ujumbe wa uthibitisho hivi karibuni.')

    def languageChangeSuccess(self):
        if self.lang == 'SW':
            return self.get_response('Language changed successfully')
        elif self.lang == 'EN':
            return self.get_response('Lugha imebadilika kwa mafanikio')

    def languageChangeError(self):
        if self.lang == 'SW':
            return self.get_response('Language change failed, Please try again')
        elif self.lang == 'UEN':
            return self.get_response('Lugha haijabadilika, Tafadhali jaribu tena')
