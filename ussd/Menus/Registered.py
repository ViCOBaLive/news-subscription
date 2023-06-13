
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


class RegisteredMenu:
    def __init__(self, lang, base_url, phone_number, request):
        self.lang = lang
        self.base_url = base_url
        self.phone_number = normalize_phone_number(phone_number)
        self.request = request

    def get_main_menu(self, text):
        if self.lang == 'EN':
            return f"CON {text} \n"
        elif self.lang == 'SW':
            return f"CON {text} \n"

    def get_menu(self, text, more=None):
        if more == None:
            pass
        if self.lang == 'EN':
            return f"CON {text}\n98. Go Back \n99.Main Menu \n"
        elif self.lang == 'SW':
            return f"CON {text}\n98. Rudi Nyuma \n99. Menu Kuu \n"

    # menus for registered users

    
    def MainMenu(self, groupName):
        if self.lang == 'EN':
            return self.get_main_menu(f'Welcome to {groupName} Please Subscribe to. \n'
                                      '1. Politics \n'
                                      '2. Health \n'
                                      '3. Sports \n'
                                      '4. Business and Finance \n'
                                      '5. Badili Lugha \n'

            )
        elif self.lang == 'SW':
            return self.get_main_menu(f'Karibu {groupName} ,Tafadhali chagua huduma. \n'
                                      '1. Siasa \n'
                                      '2. Afya \n'
                                      '3. Michezo \n'
                                      '4. Biashara \n'
                                      '5. Change Language \n'
                                      )

    def PoliticsMenu(self):
        if self.lang == 'EN':
            return self.get_menu('Please choose an account. \n'
                                 '1. Domestic \n'
                                 '2. International \n')
        elif self.lang == 'SW':
            return self.get_menu('Tafadhali chagua akaunti. \n'
                                 '1. Siasa za Nyumbani \n'
                                 '2. Siasa za Nje  \n'
                                 )

    def HealthMenu(self):
        if self.lang == 'EN':
            return self.get_menu('Please choose an Health News option. \n'
                                 '1. Self Health \n'
                                 '2. Food and Diet \n'

                                 )
        elif self.lang == 'SW':
            return self.get_menu('Tafadhali chagua chaguo. \n'
                                 '1. Afya Binafsi \n'
                                 '2.  Afya ya Mlo (Diet) \n'
                                 )
    def SportsMenu(self):
        if self.lang == 'EN':
            return self.get_menu('Please choose an Sports News option. \n'
                                 '1. Domestic Sports \n'
                                 '2. Internations Sports \n'

                                 )
        elif self.lang == 'SW':
            return self.get_menu('Tafadhali chagua chaguo. \n'
                                 '1. Michezo ya nyumbani \n'
                                 '2.  Michezo yakimataifa \n'
                                 )
    
    def BusinessMenu(self):
        if self.lang == 'EN':
            return self.get_menu('Please choose an Business News option. \n'
                                 '1. Stock Market \n'
                                 '2. Currency Exchange Rates \n'
                                 '3. Daily Businness Tips \n'

                                 )
        elif self.lang == 'SW':
            return self.get_menu('Tafadhali chagua chaguo. \n'
                                 '1. Soko la Hisa\n'
                                 '2. Thamani za Fedha  \n'
                                 '3. Dodoso za Biashara '
                                 )

    def ApprovalMenu(self,subscriptions):
        if self.lang == 'EN':
            return self.get_menu(f'You are about to subscribe to {subscriptions} News.\n'
                                 '1. Confirm \n'
                                 )
        elif self.lang == 'SW':
            return self.get_menu(f'Unaenda kujisajili na taarifa za {subscriptions}.\n'
                                 '1. Thibitisha \n'
                                 )

    def SubSucccesfullRes(self, product):
        if self.lang == 'EN':
            return self.get_menu(f'You have successfully subscribed to {product}, Feel free to Unsubscribe any time\n'
                                 )
        elif self.lang == 'SW':
            return self.get_menu(f'Umefanikiwa kujisajili na  {product}. Kua huru kujitoa mda wowote. \n'
                                 )

    def SubFailedRes(self):
        if self.lang == 'EN':
            return self.get_menu(f'Failed to subscribe to the news , Please try again\n'
                                 )
        elif self.lang == 'SW':
            return self.get_menu(f'meshindwa kukusajili, tafadhali jaribu tena ! \n'
                                 )



