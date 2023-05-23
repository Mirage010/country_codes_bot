import requests
from bs4 import BeautifulSoup as BS
import telebot
from telebot import types
import emoji
import lxml

bot = telebot.TeleBot('TOKEN')

url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=GEL'
r = requests.get(url)
soup = BS(r.text, 'lxml')
curs = soup.find("p", {"class" : "result__BigRate-sc-1bsijpp-1 iGrAod"}).text



url1 = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR'
d = requests.get(url1)
soup = BS(d.text, 'lxml')
curseur = soup.find("p", {"class" : "result__BigRate-sc-1bsijpp-1 iGrAod"}).text


url3 = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=GEL&To=USD'
m = requests.get(url3)
soup = BS(m.text, 'lxml')
curselari = soup.find("p", {"class" : "result__BigRate-sc-1bsijpp-1 iGrAod"}).text



url4 = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=GEL&To=EUR'
w = requests.get(url4)
soup = BS(w.text, 'lxml')
curselarieur = soup.find("p", {"class" : "result__BigRate-sc-1bsijpp-1 iGrAod"}).text
##############################################################################################

url5 = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=GEL'
t = requests.get(url5)
soup = BS(t.text, 'lxml')
eurgell = soup.find("p", {"class" : "result__BigRate-sc-1bsijpp-1 iGrAod"}).text


url6 = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD'
p = requests.get(url6)
soup = BS(p.text, 'lxml')
eurusd = soup.find("p", {"class" : "result__BigRate-sc-1bsijpp-1 iGrAod"}).text



@bot.message_handler(commands=['start'])
def entry(message):
    if message.text == '/start':
        b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1.row(types.KeyboardButton('Exchange rate'), types.KeyboardButton('Country/country codes'))
        msg = bot.send_message(message.chat.id, emoji.emojize(':United_Kingdom:') + 'Welcome to GLOBALCELL info BOT on Telegram')
        bot.send_message(message.chat.id, emoji.emojize(':Georgia:') + 'მოგესალმებით "გლობალსელის" საინფორმაციო ბოტ-არხზე ტელეგრამში', reply_markup=b1)
        bot.send_message(message.chat.id, 'Click the button for information')
        bot.register_next_step_handler(msg, menumessage)


def mainmenu(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.row(types.KeyboardButton('Exchange rate'), types.KeyboardButton('Country/country codes'))
    msg = bot.send_message(message.chat.id, f'Home', reply_markup=b1)
    bot.register_next_step_handler(msg, menumessage)





def menumessage(message):
    if message.text == 'Exchange rate':
        curmenu(message)
    elif message.text == 'Country/country codes':
        codesstep2(message)
    else:
        mainmenu(message)





def curmenu(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('GEL'), types.KeyboardButton('USD'), types.KeyboardButton('EUR'))
    b1.row(types.KeyboardButton('Home'))
    msg = bot.send_message(message.chat.id, 'Select a currency to view the exchange rate', reply_markup=b1)
    bot.register_next_step_handler(msg, gelrates)








def gelrates(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Back'))
    if message.text == 'GEL':
        go_main = bot.send_message(message.chat.id, f'1 GEL -- {curselari} \n'
                                      f'1 GEL -- {curselarieur}', reply_markup=b1)

        bot.register_next_step_handler(go_main, curmenu)


    elif message.text == 'USD':
        go_main = bot.send_message(message.chat.id, f'1 USD -- {curs} \n'
                                          f'1 USD -- {curseur}', reply_markup=b1)
        bot.register_next_step_handler(go_main, curmenu)
    elif message.text == 'EUR':
        go_main = bot.send_message(message.chat.id, f'1 EUR -- {eurgell} \n'
                                          f'1 EUR -- {eurusd}', reply_markup=b1)
        bot.register_next_step_handler(go_main, curmenu)

    elif message.text == 'Back':
        curmenu(message)

    else:
        mainmenu(message)







def eurrates(message):
    bot.send_message(message.chat.id, f'1 EUR -- {eurgell} \n'
                                      f'1 EUR -- {eurusd}')




#####################################################################



def codesstep2(message):
    msg = bot.send_message(message.chat.id, f'Enter country or country code:\n'
                                            f'example: "Georgia" or "+995"')
    bot.register_next_step_handler(msg, codes)





def correct(message):
    msg = bot.send_message(message.chat.id, 'Enter valid information')
    bot.register_next_step_handler(msg, codes)


def enter(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Back'))
    msg = bot.send_message(message.chat.id, 'Please enter Country or Country code', reply_markup=b1)
    bot.register_next_step_handler(msg, codes)














def codes(message):
    try:
##############################################################################################################
###Afghanistan                                                                                               #
##############################################################################################################
        if message.text == 'Afghanistan'  or message.text =='afghanistan':
            bot.send_message(message.chat.id, f'Country CODE : +93\n'
                                              f'ISO CODE : AF/AFG')
            enter(message)


        elif message.text == '93' or message.text == '+93':
            bot.send_message(message.chat.id, f'Country : Afghanistan\n'
                                              f'ISO CODE : AF/AFG')
            enter(message)


##############################################################################################################
# albania                                                                                             #
##############################################################################################################

        elif message.text == 'Albania'  or message.text == 'albania':
            bot.send_message(message.chat.id, f'Country CODE : +355\n'
                                              f'ISO CODE : AL/ALB')
            enter(message)



        elif message.text == '355' or message.text == '+355':
            bot.send_message(message.chat.id, f'Country  : Albania\n'
                                              f'ISO CODE : AL/ALB')
            enter(message)
##############################################################################################################
# Algeria                                                                                             #
##############################################################################################################

        elif message.text == 'Algeria'  or message.text == 'algeria':
            bot.send_message(message.chat.id, f'Country CODE : +213\n'
                                              f'ISO CODE : DZ/DZA')
            enter(message)



        elif message.text == '213' or message.text == '+213':
            bot.send_message(message.chat.id, f'Country  : Algeria\n'
                                              f'ISO CODE : DZ/DZA')
            enter(message)

##############################################################################################################
# american samoa                                                                                             #
##############################################################################################################

        elif message.text == 'American Samoa' or message.text == 'American samoa' or message.text == 'american samoa':
            bot.send_message(message.chat.id, f'Country CODE : +1-684\n'
                                              f'ISO CODE : AS/ASM')
            enter(message)



        elif message.text == '1-684' or message.text == '+1-684':
            bot.send_message(message.chat.id, f'Country  : American Samoa\n'
                                              f'ISO CODE : AS/ASM')
            enter(message)

##############################################################################################################
# Andora                                                                                           #
##############################################################################################################

        elif message.text == 'Andora' or message.text == 'andora':
            bot.send_message(message.chat.id, f'Country CODE : +376\n'
                                              f'ISO CODE : AD/AND')
            enter(message)



        elif message.text == '376' or message.text == '+376':
            bot.send_message(message.chat.id, f'Country  : Andora\n'
                                              f'ISO CODE : AD/AND')
            enter(message)

##############################################################################################################
# ANGOLA                                                                                         #
##############################################################################################################

        elif message.text == 'Angola' or message.text == 'angola':
            bot.send_message(message.chat.id, f'Country CODE : +244\n'
                                              f'ISO CODE : AO/AGO')
            enter(message)



        elif message.text == '244' or message.text == '+244':
            bot.send_message(message.chat.id, f'Country  : Angola\n'
                                              f'ISO CODE : AO/AGO')
            enter(message)

##############################################################################################################
# Anguilla                                                                                         #
##############################################################################################################

        elif message.text == 'Anguilla' or message.text == 'anguilla':
            bot.send_message(message.chat.id, f'Country CODE : +1-264\n'
                                              f'ISO CODE : AI/AIA')
            enter(message)



        elif message.text == '1-264' or message.text == '+1-264':
            bot.send_message(message.chat.id, f'Country  : Anguilla\n'
                                              f'ISO CODE : AI/AIA')
            enter(message)

##############################################################################################################
# Antarctica                                                                                         #
##############################################################################################################

        elif message.text == 'Antarctica' or message.text == 'antarctica':
            bot.send_message(message.chat.id, f'Country CODE : +672\n'
                                              f'ISO CODE : AQ/ATA')
            enter(message)



        elif message.text == '672' or message.text == '+672':
            bot.send_message(message.chat.id, f'Country  : Antarctica\n'
                                              f'ISO CODE : AI/AIA')
            enter(message)

##############################################################################################################
# Antigua and Barbuda                                                                                     #
##############################################################################################################

        elif message.text == 'Antigua and Barbuda' or message.text == 'Antigua and barbuda' or message.text == 'antigua and barbuda':
            bot.send_message(message.chat.id, f'Country CODE : +1-268\n'
                                              f'ISO CODE : AG/ATG')
            enter(message)



        elif message.text == '1-268' or message.text == '+1-268':
            bot.send_message(message.chat.id, f'Country  : Antigua and Barbuda\n'
                                              f'ISO CODE : AG/ATG')
            enter(message)

##############################################################################################################
# Argentina                                                                                    #
##############################################################################################################

        elif message.text == 'Argentina' or message.text == 'argentina':
            bot.send_message(message.chat.id, f'Country CODE : +54\n'
                                              f'ISO CODE : AR/ARG')
            enter(message)



        elif message.text == '54' or message.text == '+54':
            bot.send_message(message.chat.id, f'Country  : Argentina\n'
                                              f'ISO CODE : AR/ARG')
            enter(message)

##############################################################################################################
# Armenia                                                                                    #
##############################################################################################################

        elif message.text == 'Armenia' or message.text == 'armenia':
            bot.send_message(message.chat.id, f'Country CODE : +374\n'
                                              f'ISO CODE : AM/ARM')
            enter(message)



        elif message.text == '374' or message.text == '+374':
            bot.send_message(message.chat.id, f'Country  : Armenia\n'
                                              f'ISO CODE : AM/ARM')
            enter(message)

##############################################################################################################
# Armenia                                                                                    #
##############################################################################################################

        elif message.text == 'Armenia' or message.text == 'armenia':
            bot.send_message(message.chat.id, f'Country CODE : +374\n'
                                              f'ISO CODE : AM/ARM')
            enter(message)



        elif message.text == '374' or message.text == '+374':
            bot.send_message(message.chat.id, f'Country  : Armenia\n'
                                              f'ISO CODE : AM/ARM')
            enter(message)

##############################################################################################################
# Aruba                                                                                    #
##############################################################################################################

        elif message.text == 'Aruba' or message.text == 'aruba':
            bot.send_message(message.chat.id, f'Country CODE : +297\n'
                                              f'ISO CODE : AW/ABW')
            enter(message)



        elif message.text == '297' or message.text == '+297':
            bot.send_message(message.chat.id, f'Country  : Aruba\n'
                                              f'ISO CODE : AW/ABW')
            enter(message)

##############################################################################################################
# australia                                                                                    #
##############################################################################################################

        elif message.text == 'Australia' or message.text == 'australia':
            bot.send_message(message.chat.id, f'Country CODE : +61\n'
                                              f'ISO CODE : AU/AUS')
            enter(message)



        elif message.text == '61' or message.text == '+61':
            bot.send_message(message.chat.id, f'Country  : Australia\n'
                                              f'ISO CODE : AU/AUS')
            bot.send_message(message.chat.id, f'Country  : Christmas Island\n'
                                              f'ISO CODE : CX/CXR')
            bot.send_message(message.chat.id, f'Country  : Cocos Island\n'
                                              f'ISO CODE : CC/CCK')
            enter(message)

##############################################################################################################
# austria                                                                                   #
##############################################################################################################

        elif message.text == 'Austria' or message.text == 'austria':
            bot.send_message(message.chat.id, f'Country CODE : +43\n'
                                              f'ISO CODE : AT/AUT')
            enter(message)



        elif message.text == '43' or message.text == '+43':
            bot.send_message(message.chat.id, f'Country  : Austria\n'
                                              f'ISO CODE : AT/AUT')
            enter(message)

##############################################################################################################
# azerbaijan                                                                                   #
##############################################################################################################

        elif message.text == 'Azerbaijan' or message.text == 'azerbaijan':
            bot.send_message(message.chat.id, f'Country CODE : +994\n'
                                              f'ISO CODE : AZ/AZE')
            enter(message)



        elif message.text == '994' or message.text == '+994':
            bot.send_message(message.chat.id, f'Country  : Azerbaijan\n'
                                              f'ISO CODE : AZ/AZE')
            enter(message)

##############################################################################################################
# Bahamas                                                                              #
##############################################################################################################

        elif message.text == 'Bahamas' or message.text == 'bahamas':
            bot.send_message(message.chat.id, f'Country CODE : +1-242\n'
                                              f'ISO CODE : BS/BHS')
            enter(message)



        elif message.text == '1-242' or message.text == '+1-242':
            bot.send_message(message.chat.id, f'Country  : Bahamas\n'
                                              f'ISO CODE : BS/BHS')
            enter(message)

##############################################################################################################
# Bahrain                                                                              #
##############################################################################################################

        elif message.text == 'Bahrain' or message.text == 'bahrain':
            bot.send_message(message.chat.id, f'Country CODE : +973\n'
                                              f'ISO CODE : BH/BHR')
            enter(message)



        elif message.text == '973' or message.text == '+973':
            bot.send_message(message.chat.id, f'Country  : Bahrain\n'
                                              f'ISO CODE : BH/BHR')
            enter(message)

##############################################################################################################
# Bangladesh                                                                           #
##############################################################################################################

        elif message.text == 'Bangladesh' or message.text == 'bangladesh':
            bot.send_message(message.chat.id, f'Country CODE : +880\n'
                                              f'ISO CODE : BD/BGD')
            enter(message)



        elif message.text == '880' or message.text == '+880':
            bot.send_message(message.chat.id, f'Country  : Bangladesh\n'
                                              f'ISO CODE : BD/BGD')
            enter(message)


##############################################################################################################
# Barbados                                                                          #
##############################################################################################################

        elif message.text == 'Barbados' or message.text == 'barbados':
            bot.send_message(message.chat.id, f'Country CODE : +1-246\n'
                                              f'ISO CODE : BB/BRB')
            enter(message)



        elif message.text == '1-246' or message.text == '+1-246':
            bot.send_message(message.chat.id, f'Country  : Barbados\n'
                                              f'ISO CODE : BB/BRB')
            enter(message)


##############################################################################################################
# Belarus                                                                     #
##############################################################################################################

        elif message.text == 'Belarus' or message.text == 'belarus':
            bot.send_message(message.chat.id, f'Country CODE : +375\n'
                                              f'ISO CODE : BY/BLR')
            enter(message)



        elif message.text == '375' or message.text == '+375':
            bot.send_message(message.chat.id, f'Country  : Belarus\n'
                                              f'ISO CODE : BY/BLR')
            enter(message)

##############################################################################################################
# Belgium                                                                   #
##############################################################################################################

        elif message.text == 'Belgium' or message.text == 'belgium':
            bot.send_message(message.chat.id, f'Country CODE : +32\n'
                                              f'ISO CODE : BE/BEL')
            enter(message)



        elif message.text == '32' or message.text == '+32':
            bot.send_message(message.chat.id, f'Country  : Belgium\n'
                                              f'ISO CODE : BE/BEL')
            enter(message)

##############################################################################################################
# Belize                                                                 #
##############################################################################################################

        elif message.text == 'Belize' or message.text == 'belize':
            bot.send_message(message.chat.id, f'Country CODE : +501\n'
                                              f'ISO CODE : BZ/BLZ')
            enter(message)



        elif message.text == '501' or message.text == '+501':
            bot.send_message(message.chat.id, f'Country  : Belize\n'
                                              f'ISO CODE : BZ/BLZ')
            enter(message)

##############################################################################################################
# Benin                                                                  #
##############################################################################################################

        elif message.text == 'Benin' or message.text == 'benin':
            bot.send_message(message.chat.id, f'Country CODE : +229\n'
                                              f'ISO CODE : BJ/BEN')
            enter(message)



        elif message.text == '229' or message.text == '+229':
            bot.send_message(message.chat.id, f'Country  : Belize\n'
                                              f'ISO CODE : BJ/BEN')
            enter(message)

##############################################################################################################
# Bermuda                                                                 #
##############################################################################################################

        elif message.text == 'Bermuda' or message.text == 'bermuda':
            bot.send_message(message.chat.id, f'Country CODE : +1-441\n'
                                              f'ISO CODE : BM/BMU')
            enter(message)



        elif message.text == '1-441' or message.text == '+1-441':
            bot.send_message(message.chat.id, f'Country  : Bermuda\n'
                                              f'ISO CODE : BM/BMU')
            enter(message)


##############################################################################################################
# Bhutan                                                                 #
##############################################################################################################

        elif message.text == 'Bhutan' or message.text == 'bhutan':
            bot.send_message(message.chat.id, f'Country CODE : +975\n'
                                              f'ISO CODE : BT/BTN')
            enter(message)



        elif message.text == '975' or message.text == '+975':
            bot.send_message(message.chat.id, f'Country  : Bhutan\n'
                                              f'ISO CODE : BT/BTN')
            enter(message)

##############################################################################################################
# Bolivia                                                                 #
##############################################################################################################

        elif message.text == 'Bolivia' or message.text == 'bolivia':
            bot.send_message(message.chat.id, f'Country CODE : +591\n'
                                              f'ISO CODE : BO/BOL')
            enter(message)



        elif message.text == '591' or message.text == '+591':
            bot.send_message(message.chat.id, f'Country  : Bolivia\n'
                                              f'ISO CODE : BO/BOL')
            enter(message)

##############################################################################################################
# Bosnia and Herzegovina                                                              #
##############################################################################################################

        elif message.text == 'Bosnia and Herzegovina' or message.text == 'Bosnia and herzegovina' or message.text == 'bosnia and herzegovina' or message.text == 'Bosnia And Herzegovina':
            bot.send_message(message.chat.id, f'Country CODE : +387\n'
                                              f'ISO CODE : BA/BIH')
            enter(message)



        elif message.text == '387' or message.text == '+387':
            bot.send_message(message.chat.id, f'Country  : Bosnia and Herzegovina\n'
                                              f'ISO CODE : BA/BIH')
            enter(message)

##############################################################################################################
# botswana                                                       #
##############################################################################################################

        elif message.text == 'Botswana' or message.text == 'botswana':
            bot.send_message(message.chat.id, f'Country CODE : +267\n'
                                              f'ISO CODE : BW/BWA')
            enter(message)



        elif message.text == '267' or message.text == '+267':
            bot.send_message(message.chat.id, f'Country  : Botswana\n'
                                              f'ISO CODE : BW/BWA')
            enter(message)

##############################################################################################################
# Brazil                                                           #
##############################################################################################################

        elif message.text == 'Brazil' or message.text == 'Brazil':
            bot.send_message(message.chat.id, f'Country CODE : +55\n'
                                              f'ISO CODE : BR/BRA')
            enter(message)



        elif message.text == '55' or message.text == '+55':
            bot.send_message(message.chat.id, f'Country  : Brazil\n'
                                              f'ISO CODE : BR/BRA')
            enter(message)

##############################################################################################################
# British Indian Ocean Territory                                                          #
##############################################################################################################

        elif message.text == 'British Indian Ocean Territory' or message.text == 'british indian ocean territory' or message.text == 'British indian ocean territory':
            bot.send_message(message.chat.id, f'Country CODE : +246\n'
                                              f'ISO CODE : IO/IOT')
            enter(message)



        elif message.text == '246' or message.text == '+246':
            bot.send_message(message.chat.id, f'Country  : British Indian Ocean Territory\n'
                                              f'ISO CODE : IO/IOT')
            enter(message)


##############################################################################################################
# British virgin islands                                                      #
##############################################################################################################

        elif message.text == 'British Virgin Islands' or message.text == 'British virgin islands' or message.text == 'british virgin islands':
            bot.send_message(message.chat.id, f'Country CODE : +1-284\n'
                                              f'ISO CODE : VG/VCB')
            enter(message)



        elif message.text == '1-284' or message.text == '+1-284':
            bot.send_message(message.chat.id, f'Country  : British Virgin Islands\n'
                                              f'ISO CODE : VG/VCB')
            enter(message)

##############################################################################################################
# Brunei                                                     #
##############################################################################################################

        elif message.text == 'Brunei' or message.text == 'brunei':
            bot.send_message(message.chat.id, f'Country CODE : +673\n'
                                              f'ISO CODE : BN/BRN')
            enter(message)



        elif message.text == '673' or message.text == '+673':
            bot.send_message(message.chat.id, f'Country  : Brunei\n'
                                              f'ISO CODE : BN/BRN')
            enter(message)

##############################################################################################################
# Bulgaria                                                     #
##############################################################################################################

        elif message.text == 'Bulgaria' or message.text == 'bulgaria':
            bot.send_message(message.chat.id, f'Country CODE : +359\n'
                                              f'ISO CODE : BG/BGR')
            enter(message)



        elif message.text == '359' or message.text == '+359':
            bot.send_message(message.chat.id, f'Country  : Bulgaria\n'
                                              f'ISO CODE : BG/BGR')
            enter(message)


##############################################################################################################
# Burkina Faso                                                    #
##############################################################################################################

        elif message.text == 'Burkina Faso' or message.text == 'Burkina faso' or message.text == 'burkina faso':
            bot.send_message(message.chat.id, f'Country CODE : +226\n'
                                              f'ISO CODE : BF/BFA')
            enter(message)



        elif message.text == '226' or message.text == '+226':
            bot.send_message(message.chat.id, f'Country  : Burkina Faso\n'
                                              f'ISO CODE : BF/BFA')
            enter(message)

##############################################################################################################
# Burundi                                                    #
##############################################################################################################

        elif message.text == 'Burundi' or message.text == 'burundi':
            bot.send_message(message.chat.id, f'Country CODE : +257\n'
                                              f'ISO CODE : BI/BDI')
            enter(message)



        elif message.text == '257' or message.text == '+257':
            bot.send_message(message.chat.id, f'Country  : Burundi\n'
                                              f'ISO CODE : BI/BDI')
            enter(message)

##############################################################################################################
# Cambodia                                                 #
##############################################################################################################

        elif message.text == 'Cambodia' or message.text == 'cambodia':
            bot.send_message(message.chat.id, f'Country CODE : +855\n'
                                              f'ISO CODE : KH/KHM')
            enter(message)



        elif message.text == '855' or message.text == '+855':
            bot.send_message(message.chat.id, f'Country  : Cambodia\n'
                                              f'ISO CODE : KH/KHM')
            enter(message)

##############################################################################################################
# Camerroon                                                 #
##############################################################################################################

        elif message.text == 'Cameroon' or message.text == 'cameroon':
            bot.send_message(message.chat.id, f'Country CODE : +237\n'
                                              f'ISO CODE : CM/CMR')
            enter(message)



        elif message.text == '237' or message.text == '+237':
            bot.send_message(message.chat.id, f'Country  : Cameroon\n'
                                              f'ISO CODE : CM/CMR')
            enter(message)

##############################################################################################################
# Canada                                                #
##############################################################################################################

        elif message.text == 'Canada' or message.text == 'canada':
            bot.send_message(message.chat.id, f'Country CODE : +1\n'
                                              f'ISO CODE : CA/CAN')
            enter(message)



        elif message.text == '1' or message.text == '+1':
            bot.send_message(message.chat.id, f'Country  : United States\n'
                                              f'ISO CODE : US/USA')
            bot.send_message(message.chat.id, f'Country  : Canada\n'
                                              f'ISO CODE : CA/CAN')
            enter(message)


##############################################################################################################
# Cape Verde                                               #
##############################################################################################################

        elif message.text == 'Cape Verde' or message.text == 'Cape verde' or message.text == 'cape verde':
            bot.send_message(message.chat.id, f'Country CODE : +238\n'
                                              f'ISO CODE : CV/CPV')
            enter(message)



        elif message.text == '237' or message.text == '+238':
            bot.send_message(message.chat.id, f'Country  : Cape Verde\n'
                                              f'ISO CODE : CV/CPV')
            enter(message)


##############################################################################################################
# Cayman Islands                                               #
##############################################################################################################

        elif message.text == 'Cayman Islands' or message.text == 'Cayman islands' or message.text == 'cayman islands':
            bot.send_message(message.chat.id, f'Country CODE : +1-345\n'
                                              f'ISO CODE : KY/CYM')
            enter(message)



        elif message.text == '1-345' or message.text == '+1-345':
            bot.send_message(message.chat.id, f'Country  : Cayman Islands\n'
                                              f'ISO CODE : KY/CYM')
            enter(message)


##############################################################################################################
# Central African Republic                                              #
##############################################################################################################

        elif message.text == 'Central African Republic' or message.text == 'Central african republic' or message.text == 'Central african republic':
            bot.send_message(message.chat.id, f'Country CODE : +236\n'
                                              f'ISO CODE : CF/CAF')
            enter(message)



        elif message.text == '236' or message.text == '+236':
            bot.send_message(message.chat.id, f'Country  : Central African Republic\n'
                                              f'ISO CODE : CF/CAF')
            enter(message)

##############################################################################################################
# Chad                                            #
##############################################################################################################

        elif message.text == 'Chad' or message.text == 'chad':
            bot.send_message(message.chat.id, f'Country CODE : +235\n'
                                              f'ISO CODE : TD/TCD')
            enter(message)



        elif message.text == '235' or message.text == '+235':
            bot.send_message(message.chat.id, f'Country  : Chad\n'
                                              f'ISO CODE : TD/TCD')
            enter(message)

##############################################################################################################
# chile                                            #
##############################################################################################################

        elif message.text == 'Chile' or message.text == 'chile':
            bot.send_message(message.chat.id, f'Country CODE : +56\n'
                                              f'ISO CODE : CL/CHL')
            enter(message)



        elif message.text == '56' or message.text == '+56':
            bot.send_message(message.chat.id, f'Country  : Chile\n'
                                              f'ISO CODE : CL/CHL')
            enter(message)


##############################################################################################################
# china                                            #
##############################################################################################################

        elif message.text == 'China' or message.text == 'china':
            bot.send_message(message.chat.id, f'Country CODE : +86\n'
                                              f'ISO CODE : CN/CHN')
            enter(message)



        elif message.text == '86' or message.text == '+86':
            bot.send_message(message.chat.id, f'Country  : China\n'
                                              f'ISO CODE : CN/CHN')
            enter(message)

##############################################################################################################
# Christmas Island                                            #
##############################################################################################################

        elif message.text == 'Christmas Island' or message.text == 'Christmas island' or message.text == 'christmas island':
            bot.send_message(message.chat.id, f'Country CODE : +86\n'
                                              f'ISO CODE : CX/CXR')
            enter(message)

##############################################################################################################
# Cocos island                                            #
##############################################################################################################

        elif message.text == 'Cocos Island' or message.text == 'Cocos Island' or message.text == 'cocos island':
            bot.send_message(message.chat.id, f'Country CODE : +61\n'
                                              f'ISO CODE : CC/CCK')
            enter(message)

##############################################################################################################
# Colombia                                            #
##############################################################################################################

        elif message.text == 'Colombia' or message.text == 'colombia':
            bot.send_message(message.chat.id, f'Country CODE : +57\n'
                                              f'ISO CODE : CO/COL')
            enter(message)



        elif message.text == '57' or message.text == '+57':
            bot.send_message(message.chat.id, f'Country  : Colombia\n'
                                              f'ISO CODE : CO/COL')
            enter(message)

##############################################################################################################
# Comoros                                            #
##############################################################################################################

        elif message.text == 'Comoros' or message.text == 'Comoros':
            bot.send_message(message.chat.id, f'Country CODE : +269\n'
                                              f'ISO CODE : KM/COM')
            enter(message)



        elif message.text == '269' or message.text == '+269':
            bot.send_message(message.chat.id, f'Country  : Comoros\n'
                                              f'ISO CODE : KM/COM')
            enter(message)

##############################################################################################################
# Cook Islands                                             #
##############################################################################################################

        elif message.text == 'Cook Islands' or message.text == 'Cook islands' or message.text == 'cook islands':
            bot.send_message(message.chat.id, f'Country CODE : +682\n'
                                              f'ISO CODE : CK/COK')
            enter(message)



        elif message.text == '682' or message.text == '+682':
            bot.send_message(message.chat.id, f'Country  : Cook Islands\n'
                                              f'ISO CODE : CK/COK')
            enter(message)

##############################################################################################################
# Costa Rica                                             #
##############################################################################################################

        elif message.text == 'Costa Rica' or message.text == 'Costa rica' or message.text == 'costa rica':
            bot.send_message(message.chat.id, f'Country CODE : +506\n'
                                              f'ISO CODE : CR/CRI')
            enter(message)



        elif message.text == '506' or message.text == '+506':
            bot.send_message(message.chat.id, f'Country  : Costa Rica\n'
                                              f'ISO CODE : CR/CRI')
            enter(message)

##############################################################################################################
# Croatia                                             #
##############################################################################################################

        elif message.text == 'Croatia' or message.text == 'croatia':
            bot.send_message(message.chat.id, f'Country CODE : +385\n'
                                              f'ISO CODE : HR/HRV')
            enter(message)



        elif message.text == '385' or message.text == '+385':
            bot.send_message(message.chat.id, f'Country  : Croatia\n'
                                              f'ISO CODE : HR/HRV')
            enter(message)

##############################################################################################################
# Cuba                                             #
##############################################################################################################

        elif message.text == 'Cuba' or message.text == 'cuba':
            bot.send_message(message.chat.id, f'Country CODE : +53\n'
                                              f'ISO CODE : CU/CUB')
            enter(message)



        elif message.text == '53' or message.text == '+53':
            bot.send_message(message.chat.id, f'Country  : Cuba\n'
                                              f'ISO CODE : CU/CUB')
            enter(message)


##############################################################################################################
# Curacao                                             #
##############################################################################################################

        elif message.text == 'Curacao' or message.text == 'Curacao':
            bot.send_message(message.chat.id, f'Country CODE : +599\n'
                                              f'ISO CODE : CW/CUW')
            enter(message)



        elif message.text == '599' or message.text == '+599':
            bot.send_message(message.chat.id, f'Country  : Curacao\n'
                                              f'ISO CODE : CW/CUW')
            bot.send_message(message.chat.id, f'Country  : Netherlands Antilles\n'
                                              f'ISO CODE : AN/NLD')
            enter(message)

##############################################################################################################
# Cyprus                                            #
##############################################################################################################

        elif message.text == 'Cyprus' or message.text == 'cyprus':
            bot.send_message(message.chat.id, f'Country CODE : +357\n'
                                              f'ISO CODE : CY/CYP')
            enter(message)



        elif message.text == '357' or message.text == '+357':
            bot.send_message(message.chat.id, f'Country  : Cyprus\n'
                                              f'ISO CODE : CY/CYP')
            enter(message)


##############################################################################################################
# Czech Republic                                            #
##############################################################################################################

        elif message.text == 'Czech Republic' or message.text == 'Czech republic' or message.text == 'czech republic' or message.text == 'Czech' or message.text == 'czech':
            bot.send_message(message.chat.id, f'Country CODE : +420\n'
                                              f'ISO CODE : CZ/CZE')
            enter(message)



        elif message.text == '420' or message.text == '+420':
            bot.send_message(message.chat.id, f'Country  : Czech Republic\n'
                                              f'ISO CODE : CZ/CZE')
            enter(message)


##############################################################################################################
# Democratic Republic of the congo                                            #
##############################################################################################################

        elif message.text == 'Democratic Republic of the Congo' or message.text == 'Democratic republic of the congo' or message.text == 'democratic republic of the congo' or message.text == 'Congo' or message.text == 'congo':
            bot.send_message(message.chat.id, f'Country CODE : +243\n'
                                              f'ISO CODE : CD/COD')
            enter(message)



        elif message.text == '243' or message.text == '+243':
            bot.send_message(message.chat.id, f'Country  : Democratic Republic of the Congo\n'
                                              f'ISO CODE : CD/COD')
            enter(message)



##############################################################################################################
# Denmark                                            #
##############################################################################################################

        elif message.text == 'Denmark' or message.text == 'denmark':
            bot.send_message(message.chat.id, f'Country CODE : +45\n'
                                              f'ISO CODE : DK/DNK')
            enter(message)



        elif message.text == '45' or message.text == '+45':
            bot.send_message(message.chat.id, f'Country  : Denmark\n'
                                              f'ISO CODE : DK/DNK')
            enter(message)



##############################################################################################################
# Djibouti                                            #
##############################################################################################################

        elif message.text == 'Djibouti' or message.text == 'djibouti':
            bot.send_message(message.chat.id, f'Country CODE : +253\n'
                                              f'ISO CODE : DJ/DJI')
            enter(message)



        elif message.text == '253' or message.text == '+253':
            bot.send_message(message.chat.id, f'Country  : djibouti\n'
                                              f'ISO CODE : DJ/DJI')
            enter(message)

##############################################################################################################
# Dominica                                            #
##############################################################################################################

        elif message.text == 'Dominica' or message.text == 'dominica':
            bot.send_message(message.chat.id, f'Country CODE : +1-767\n'
                                              f'ISO CODE : DM/DMA')
            enter(message)



        elif message.text == '1-767' or message.text == '+1-767':
            bot.send_message(message.chat.id, f'Country  : Dominica\n'
                                              f'ISO CODE : DM/DMA')
            enter(message)


##############################################################################################################
# Dominican Republic                                            #
##############################################################################################################

        elif message.text == 'Dominican Republic' or message.text == 'Dominican republic' or message.text == 'dominican republic':
            bot.send_message(message.chat.id, f'Country CODE : +1-809, 1-829, 1-849\n'
                                              f'ISO CODE : DO/DOM')
            enter(message)



        elif message.text == '1-809' or message.text == '+1-809' or message.text == '1-829' or message.text == '+1-829' or message.text == '1-849' or message.text == '+1-849':
            bot.send_message(message.chat.id, f'Country  : Dominican Republic\n'
                                              f'ISO CODE : DM/DMA')
            enter(message)

##############################################################################################################
# East Timor                                            #
##############################################################################################################

        elif message.text == 'East Timor' or message.text == 'East timor' or message.text == 'east timor':
            bot.send_message(message.chat.id, f'Country CODE : +670\n'
                                              f'ISO CODE : TL/TLS')
            enter(message)



        elif message.text == '670' or message.text == '+670':
            bot.send_message(message.chat.id, f'Country  : East Timor\n'
                                              f'ISO CODE : TL/TLS')
            enter(message)

##############################################################################################################
# Ecuador                                            #
##############################################################################################################

        elif message.text == 'Ecuador' or message.text == 'ecuador':
            bot.send_message(message.chat.id, f'Country CODE : +593\n'
                                              f'ISO CODE : EC/ECU')
            enter(message)



        elif message.text == '593' or message.text == '+593':
            bot.send_message(message.chat.id, f'Country  : Ecuador\n'
                                              f'ISO CODE : EC/ECU')
            enter(message)

##############################################################################################################
# Egypt                                            #
##############################################################################################################

        elif message.text == 'Egypt' or message.text == 'egypt':
            bot.send_message(message.chat.id, f'Country CODE : +20\n'
                                              f'ISO CODE : EG/EGY')
            enter(message)



        elif message.text == '20' or message.text == '+20':
            bot.send_message(message.chat.id, f'Country  : Egypt\n'
                                              f'ISO CODE : EG/EGY')
            enter(message)


##############################################################################################################
# El Salvador                                            #
##############################################################################################################

        elif message.text == 'El Salvador' or message.text == 'El salvador' or message.text == 'el salvador':
            bot.send_message(message.chat.id, f'Country CODE : +503\n'
                                              f'ISO CODE : SV/SLV')
            enter(message)



        elif message.text == '503' or message.text == '+503':
            bot.send_message(message.chat.id, f'Country  : El Salvador\n'
                                              f'ISO CODE : SV/SLV')
            enter(message)


##############################################################################################################
# Equatorial Guinea                                           #
##############################################################################################################

        elif message.text == 'Equatorial Guinea' or message.text == 'Equatorial guinea' or message.text == 'equatorial guinea':
            bot.send_message(message.chat.id, f'Country CODE : +240\n'
                                              f'ISO CODE : GQ/GNQ')
            enter(message)



        elif message.text == '240' or message.text == '+240':
            bot.send_message(message.chat.id, f'Country  : Equatorial Guinea\n'
                                              f'ISO CODE : GQ/GNQ')
            enter(message)


##############################################################################################################
# Eritrea                                           #
##############################################################################################################

        elif message.text == 'Eritrea' or message.text == 'eritrea':
            bot.send_message(message.chat.id, f'Country CODE : +291\n'
                                              f'ISO CODE : ER/ERI')
            enter(message)



        elif message.text == '291' or message.text == '+291':
            bot.send_message(message.chat.id, f'Country  : Eritrea\n'
                                              f'ISO CODE : ER/ERI')
            enter(message)


##############################################################################################################
# Estonia                                           #
##############################################################################################################

        elif message.text == 'Estonia' or message.text == 'estonia':
            bot.send_message(message.chat.id, f'Country CODE : +372\n'
                                              f'ISO CODE : EE/EST')
            enter(message)



        elif message.text == '372' or message.text == '+372':
            bot.send_message(message.chat.id, f'Country  : Estonia\n'
                                              f'ISO CODE : EE/EST')
            enter(message)


##############################################################################################################
# Ethiopia                                           #
##############################################################################################################

        elif message.text == 'Ethiopia' or message.text == 'ethiopia':
            bot.send_message(message.chat.id, f'Country CODE : +251\n'
                                              f'ISO CODE : ET/ETH')
            enter(message)



        elif message.text == '251' or message.text == '+251':
            bot.send_message(message.chat.id, f'Country  : Ethiopia\n'
                                              f'ISO CODE : ET/ETH')
            enter(message)


##############################################################################################################
# Falkland Islands                                          #
##############################################################################################################

        elif message.text == 'Falkland Islands' or message.text == 'Falkland islands' or message.text == 'falkland islands':
            bot.send_message(message.chat.id, f'Country CODE : +500\n'
                                              f'ISO CODE : FK/FLK')
            enter(message)



        elif message.text == '500' or message.text == '+500':
            bot.send_message(message.chat.id, f'Country  : Falkland Islands\n'
                                              f'ISO CODE : FK/FLK')
            enter(message)


##############################################################################################################
# Faroe Islands                                          #
##############################################################################################################

        elif message.text == 'Faroe Islands' or message.text == 'Faroe islands' or message.text == 'Faroe islands':
            bot.send_message(message.chat.id, f'Country CODE : +298\n'
                                              f'ISO CODE : FO/FRO')
            enter(message)



        elif message.text == '298' or message.text == '+298':
            bot.send_message(message.chat.id, f'Country  : Faroe Islands\n'
                                              f'ISO CODE : FO/FRO')
            enter(message)


##############################################################################################################
# fiji                                           #
##############################################################################################################

        elif message.text == 'Fiji' or message.text == 'fiji':
            bot.send_message(message.chat.id, f'Country CODE : +679\n'
                                              f'ISO CODE : FJ/FJI')
            enter(message)



        elif message.text == '679' or message.text == '+679':
            bot.send_message(message.chat.id, f'Country  : Fiji\n'
                                              f'ISO CODE : FJ/FJI')
            enter(message)

##############################################################################################################
# Finlad                                           #
##############################################################################################################

        elif message.text == 'Finland' or message.text == 'finland':
            bot.send_message(message.chat.id, f'Country CODE : +358\n'
                                              f'ISO CODE : FI/FIN')
            enter(message)



        elif message.text == '358' or message.text == '+358':
            bot.send_message(message.chat.id, f'Country  : Fiji\n'
                                              f'ISO CODE : FI/FIN')
            enter(message)

##############################################################################################################
# France                                           #
##############################################################################################################

        elif message.text == 'France' or message.text == 'france':
            bot.send_message(message.chat.id, f'Country CODE : +33\n'
                                              f'ISO CODE : FR/FRA')
            enter(message)



        elif message.text == '33' or message.text == '+33':
            bot.send_message(message.chat.id, f'Country  : Fiji\n'
                                              f'ISO CODE : FR/FRA')
            enter(message)

##############################################################################################################
# French Polynesia                                         #
##############################################################################################################

        elif message.text == 'French Polynesia' or message.text == 'French polynesia' or message.text == 'french polynesia':
            bot.send_message(message.chat.id, f'Country CODE : +689\n'
                                              f'ISO CODE : PF/PYF')
            enter(message)



        elif message.text == '689' or message.text == '+689':
            bot.send_message(message.chat.id, f'Country  : French Polynesia\n'
                                              f'ISO CODE : PF/PYF')
            enter(message)

##############################################################################################################
# Gabon                                           #
##############################################################################################################

        elif message.text == 'Gabon' or message.text == 'gabon':
            bot.send_message(message.chat.id, f'Country CODE : +241\n'
                                              f'ISO CODE : GA/GAB')
            enter(message)



        elif message.text == '241' or message.text == '+241':
            bot.send_message(message.chat.id, f'Country  : Gabon\n'
                                              f'ISO CODE : GA/GAB')
            enter(message)

##############################################################################################################
# Gambia                                           #
##############################################################################################################

        elif message.text == 'Gambia' or message.text == 'gambia':
            bot.send_message(message.chat.id, f'Country CODE : +220\n'
                                              f'ISO CODE : GM/GMB')
            enter(message)



        elif message.text == '220' or message.text == '+220':
            bot.send_message(message.chat.id, f'Country  : Gambia\n'
                                              f'ISO CODE : GM/GMB')
            enter(message)

##############################################################################################################
# Georgia                                           #
##############################################################################################################

        elif message.text == 'Georgia' or message.text == 'georgia' or message.text == 'Sakartvelo' or message.text == 'sakartvelo':
            bot.send_message(message.chat.id, f'Country CODE : +995\n'
                                              f'ISO CODE : GE/GEO')
            enter(message)



        elif message.text == '995' or message.text == '+995':
            bot.send_message(message.chat.id, f'Country  : Georgia\n'
                                              f'ISO CODE : GE/GEO')
            enter(message)

##############################################################################################################
# Germany                                           #
##############################################################################################################

        elif message.text == 'Germany' or message.text == 'germany':
            bot.send_message(message.chat.id, f'Country CODE : +49\n'
                                              f'ISO CODE : DE/DEU')
            enter(message)



        elif message.text == '49' or message.text == '+49':
            bot.send_message(message.chat.id, f'Country  : Germany\n'
                                              f'ISO CODE : DE/DEU')
            enter(message)


##############################################################################################################
# Ghana                                           #
##############################################################################################################

        elif message.text == 'Ghana' or message.text == 'ghana':
            bot.send_message(message.chat.id, f'Country CODE : +233\n'
                                              f'ISO CODE : GH/GHA')
            enter(message)



        elif message.text == '233' or message.text == '+233':
            bot.send_message(message.chat.id, f'Country  : Ghana\n'
                                              f'ISO CODE : GH/GHA')
            enter(message)

##############################################################################################################
# Gibraltar                                           #
##############################################################################################################

        elif message.text == 'Gibraltar' or message.text == 'gibraltar':
            bot.send_message(message.chat.id, f'Country CODE : +350\n'
                                              f'ISO CODE : GI/GIB')
            enter(message)



        elif message.text == '350' or message.text == '+350':
            bot.send_message(message.chat.id, f'Country  : Gibraltar\n'
                                              f'ISO CODE : GI/GIB')
            enter(message)

##############################################################################################################
# Greece                                           #
##############################################################################################################

        elif message.text == 'Greece' or message.text == 'greece':
            bot.send_message(message.chat.id, f'Country CODE : +30\n'
                                              f'ISO CODE : GR/GRC')
            enter(message)



        elif message.text == '30' or message.text == '+30':
            bot.send_message(message.chat.id, f'Country  : Greece\n'
                                              f'ISO CODE : GR/GRC')
            enter(message)

##############################################################################################################
# Greenland                                           #
##############################################################################################################

        elif message.text == 'Greenland' or message.text == 'greenland':
            bot.send_message(message.chat.id, f'Country CODE : +299\n'
                                              f'ISO CODE : GL/GRL')
            enter(message)



        elif message.text == '299' or message.text == '+299':
            bot.send_message(message.chat.id, f'Country  : Greenland\n'
                                              f'ISO CODE : GL/GRL')
            enter(message)


##############################################################################################################
# Grenada                                           #
##############################################################################################################

        elif message.text == 'Grenada' or message.text == 'grenada':
            bot.send_message(message.chat.id, f'Country CODE : +1-473\n'
                                              f'ISO CODE : GD/GRD')
            enter(message)



        elif message.text == '1-473' or message.text == '+1-473':
            bot.send_message(message.chat.id, f'Country  : Grenada\n'
                                              f'ISO CODE : GD/GRD')
            enter(message)

##############################################################################################################
# Guam                                           #
##############################################################################################################

        elif message.text == 'Guam' or message.text == 'guam':
            bot.send_message(message.chat.id, f'Country CODE : +1-671\n'
                                              f'ISO CODE : GU/GUM')
            enter(message)



        elif message.text == '1-671' or message.text == '+1-671':
            bot.send_message(message.chat.id, f'Country  : Grenada\n'
                                              f'ISO CODE : GU/GUM')
            enter(message)


##############################################################################################################
# Guatemala                                           #
##############################################################################################################

        elif message.text == 'Guatemala' or message.text == 'guatemala':
            bot.send_message(message.chat.id, f'Country CODE : +502\n'
                                              f'ISO CODE : GT/GTM')
            enter(message)



        elif message.text == '502' or message.text == '+502':
            bot.send_message(message.chat.id, f'Country  : Guatemala\n'
                                              f'ISO CODE : GT/GTM')
            enter(message)


##############################################################################################################
# Guernsey                                           #
##############################################################################################################

        elif message.text == 'Guernsey' or message.text == 'guernsey':
            bot.send_message(message.chat.id, f'Country CODE : +44-1481\n'
                                              f'ISO CODE : GG/GGY')
            enter(message)



        elif message.text == '44-1481' or message.text == '+44-1481':
            bot.send_message(message.chat.id, f'Country  : Guernsey\n'
                                              f'ISO CODE : GG/GGY')
            enter(message)


##############################################################################################################
# Guinea                                          #
##############################################################################################################

        elif message.text == 'Guinea' or message.text == 'Guinea':
            bot.send_message(message.chat.id, f'Country CODE : +224\n'
                                              f'ISO CODE : GN/GIN')
            enter(message)



        elif message.text == '224' or message.text == '+224':
            bot.send_message(message.chat.id, f'Country  : Guinea\n'
                                              f'ISO CODE : GN/GIN')
            enter(message)


##############################################################################################################
# Guinea-bissau                                          #
##############################################################################################################

        elif message.text == 'Guinea-Bissau' or message.text == 'Guinea-bissau' or message.text == 'guinea-bissau':
            bot.send_message(message.chat.id, f'Country CODE : +245\n'
                                              f'ISO CODE : GW/GNB')
            enter(message)



        elif message.text == '245' or message.text == '+245':
            bot.send_message(message.chat.id, f'Country  : Guinea-Bissau\n'
                                              f'ISO CODE : GW/GNB')
            enter(message)


##############################################################################################################
# Guyana                                          #
##############################################################################################################

        elif message.text == 'Guyana' or message.text == 'guyana':
            bot.send_message(message.chat.id, f'Country CODE : +592\n'
                                              f'ISO CODE : GY/GUY')
            enter(message)



        elif message.text == '592' or message.text == '+592':
            bot.send_message(message.chat.id, f'Country  : Guyana\n'
                                              f'ISO CODE : GY/GUY')
            enter(message)


##############################################################################################################
# Haiti                                          #
##############################################################################################################

        elif message.text == 'Haiti' or message.text == 'haiti':
            bot.send_message(message.chat.id, f'Country CODE : +509\n'
                                              f'ISO CODE : HT/HTI')
            enter(message)



        elif message.text == '509' or message.text == '+509':
            bot.send_message(message.chat.id, f'Country  : Guyana\n'
                                              f'ISO CODE : HT/HTI')
            enter(message)

##############################################################################################################
# Honduras                                          #
##############################################################################################################

        elif message.text == 'Honduras' or message.text == 'honduras':
            bot.send_message(message.chat.id, f'Country CODE : +504\n'
                                              f'ISO CODE : HN/HND')
            enter(message)



        elif message.text == '504' or message.text == '+504':
            bot.send_message(message.chat.id, f'Country  : Honduras\n'
                                              f'ISO CODE : HN/HND')
            enter(message)


##############################################################################################################
# Hong Kong                                          #
##############################################################################################################

        elif message.text == 'Hong Kong' or message.text == 'Hong kong' or message.text == 'hong kong':
            bot.send_message(message.chat.id, f'Country CODE : +852\n'
                                              f'ISO CODE : HK/HKG')
            enter(message)



        elif message.text == '852' or message.text == '+852':
            bot.send_message(message.chat.id, f'Country  : Hong Kong\n'
                                              f'ISO CODE : HK/HKG')
            enter(message)


##############################################################################################################
# Hungary                                         #
##############################################################################################################

        elif message.text == 'Hungary' or message.text == 'hungary':
            bot.send_message(message.chat.id, f'Country CODE : +36\n'
                                              f'ISO CODE : HU/HUN')
            enter(message)



        elif message.text == '36' or message.text == '+36':
            bot.send_message(message.chat.id, f'Country  : Hungary\n'
                                              f'ISO CODE : HU/HUN')
            enter(message)


##############################################################################################################
# Iceland                                         #
##############################################################################################################

        elif message.text == 'Iceland' or message.text == 'iceland':
            bot.send_message(message.chat.id, f'Country CODE : +354\n'
                                              f'ISO CODE : IS/ISL')
            enter(message)



        elif message.text == '354' or message.text == '+354':
            bot.send_message(message.chat.id, f'Country  : Iceland\n'
                                              f'ISO CODE : IS/ISL')
            enter(message)


##############################################################################################################
# India                                         #
##############################################################################################################

        elif message.text == 'India' or message.text == 'india':
            bot.send_message(message.chat.id, f'Country CODE : +91\n'
                                              f'ISO CODE : IN/IND')
            enter(message)



        elif message.text == '91' or message.text == '+91':
            bot.send_message(message.chat.id, f'Country  : India\n'
                                              f'ISO CODE : IN/IND')
            enter(message)


##############################################################################################################
# Indonesia                                         #
##############################################################################################################

        elif message.text == 'Indonesia' or message.text == 'indonesia':
            bot.send_message(message.chat.id, f'Country CODE : +62\n'
                                              f'ISO CODE : ID/IDN')
            enter(message)



        elif message.text == '62' or message.text == '+62':
            bot.send_message(message.chat.id, f'Country  : Indonesia\n'
                                              f'ISO CODE : ID/IDN')
            enter(message)


##############################################################################################################
# Iran                                         #
##############################################################################################################

        elif message.text == 'Iran' or message.text == 'iran':
            bot.send_message(message.chat.id, f'Country CODE : +98\n'
                                              f'ISO CODE : IR/IRN')
            enter(message)



        elif message.text == '98' or message.text == '+98':
            bot.send_message(message.chat.id, f'Country  : Iran\n'
                                              f'ISO CODE : IR/IRN')
            enter(message)

##############################################################################################################
# Iraq                                         #
##############################################################################################################

        elif message.text == 'Iraq' or message.text == 'Iraq':
            bot.send_message(message.chat.id, f'Country CODE : +964\n'
                                              f'ISO CODE : IQ/IRQ')
            enter(message)



        elif message.text == '964' or message.text == '+964':
            bot.send_message(message.chat.id, f'Country  : Iraq\n'
                                              f'ISO CODE : IQ/IRQ')
            enter(message)


##############################################################################################################
# Ireland                                         #
##############################################################################################################

        elif message.text == 'Ireland' or message.text == 'ireland':
            bot.send_message(message.chat.id, f'Country CODE : +353\n'
                                              f'ISO CODE : IE/IRL')
            enter(message)



        elif message.text == '353' or message.text == '+353':
            bot.send_message(message.chat.id, f'Country  : Ireland\n'
                                              f'ISO CODE : IE/IRL')
            enter(message)


##############################################################################################################
# Isle of Man                                         #
##############################################################################################################

        elif message.text == 'Isle of Man' or message.text == 'Isle of man' or message.text == 'isle of man':
            bot.send_message(message.chat.id, f'Country CODE : +44-1624\n'
                                              f'ISO CODE : IM/IMN')
            enter(message)



        elif message.text == '44-1624' or message.text == '+44-1624':
            bot.send_message(message.chat.id, f'Country  : Isle of Man\n'
                                              f'ISO CODE : IM/IMN')
            enter(message)


##############################################################################################################
# Israel                                         #
##############################################################################################################

        elif message.text == 'Israel' or message.text == 'israel':
            bot.send_message(message.chat.id, f'Country CODE : +972\n'
                                              f'ISO CODE : IL/ISR')
            enter(message)



        elif message.text == '972' or message.text == '+972':
            bot.send_message(message.chat.id, f'Country  : Israel\n'
                                              f'ISO CODE : IL/ISR')
            enter(message)


##############################################################################################################
# Italy                                         #
##############################################################################################################

        elif message.text == 'Italy' or message.text == 'italy':
            bot.send_message(message.chat.id, f'Country CODE : +39\n'
                                              f'ISO CODE : IT/ITA')
            enter(message)



        elif message.text == '39' or message.text == '+39':
            bot.send_message(message.chat.id, f'Country  : Italy\n'
                                              f'ISO CODE : IT/ITA')
            enter(message)

##############################################################################################################
# Ivory Coast                                         #
##############################################################################################################

        elif message.text == 'Ivory Coast' or message.text == 'Ivory coast' or message.text == 'ivory coast':
            bot.send_message(message.chat.id, f'Country CODE : +225\n'
                                              f'ISO CODE : CI/CIV')
            enter(message)



        elif message.text == '225' or message.text == '+225':
            bot.send_message(message.chat.id, f'Country  : Ivory Coast\n'
                                              f'ISO CODE : CI/CIV')
            enter(message)


##############################################################################################################
# Jamaica                                        #
##############################################################################################################

        elif message.text == 'Jamaica' or message.text == 'jamaica':
            bot.send_message(message.chat.id, f'Country CODE : +1-876\n'
                                              f'ISO CODE : JM/JAM')
            enter(message)



        elif message.text == '1-876' or message.text == '+1-876':
            bot.send_message(message.chat.id, f'Country  : Jamaica\n'
                                              f'ISO CODE : JM/JAM')
            enter(message)


##############################################################################################################
# Japan                                        #
##############################################################################################################

        elif message.text == 'Japan' or message.text == 'japan':
            bot.send_message(message.chat.id, f'Country CODE : +81\n'
                                              f'ISO CODE : JP/JPN')
            enter(message)



        elif message.text == '81' or message.text == '+81':
            bot.send_message(message.chat.id, f'Country  : Japan\n'
                                              f'ISO CODE : JP/JPN')
            enter(message)


##############################################################################################################
# Jersey                                        #
##############################################################################################################

        elif message.text == 'Jersey' or message.text == 'jersey':
            bot.send_message(message.chat.id, f'Country CODE : +44-1534\n'
                                              f'ISO CODE : JE/JEY')
            enter(message)



        elif message.text == '44-1534' or message.text == '+44-1534':
            bot.send_message(message.chat.id, f'Country  : Jersey\n'
                                              f'ISO CODE : JE/JEY')
            enter(message)

##############################################################################################################
# Jordan                                        #
##############################################################################################################

        elif message.text == 'Jordan' or message.text == 'jordan':
            bot.send_message(message.chat.id, f'Country CODE : +962\n'
                                              f'ISO CODE : JO/JOR')
            enter(message)



        elif message.text == '962' or message.text == '+962':
            bot.send_message(message.chat.id, f'Country  : Jordan\n'
                                              f'ISO CODE : JO/JOR')
            enter(message)

##############################################################################################################
# Kazakhstan                                        #
##############################################################################################################

        elif message.text == 'Kazakhstan' or message.text == 'kazakhstan':
            bot.send_message(message.chat.id, f'Country CODE : +7\n'
                                              f'ISO CODE : KZ/KAZ')
            enter(message)



        elif message.text == '7' or message.text == '+7':
            bot.send_message(message.chat.id, f'Country  : Kazakhstan\n'
                                              f'ISO CODE : KZ/KAZ')
            bot.send_message(message.chat.id, f'Country  : Russia\n'
                                              f'ISO CODE : RU/RUS')
            enter(message)

##############################################################################################################
# Kenya                                        #
##############################################################################################################

        elif message.text == 'Kenya' or message.text == 'kenya':
            bot.send_message(message.chat.id, f'Country CODE : +254\n'
                                              f'ISO CODE : KE/KEN')
            enter(message)



        elif message.text == '254' or message.text == '+254':
            bot.send_message(message.chat.id, f'Country  : Kenya\n'
                                              f'ISO CODE : KE/KEN')
            enter(message)


##############################################################################################################
# Kiribati                                        #
##############################################################################################################

        elif message.text == 'Kiribati' or message.text == 'kiribati':
            bot.send_message(message.chat.id, f'Country CODE : +686\n'
                                              f'ISO CODE : KI/KIR')
            enter(message)



        elif message.text == '686' or message.text == '+686':
            bot.send_message(message.chat.id, f'Country  : Kiribati\n'
                                              f'ISO CODE : KI/KIR')
            enter(message)

##############################################################################################################
# Kosovo                                     #
##############################################################################################################

        elif message.text == 'Kosovo' or message.text == 'kosovo':
            bot.send_message(message.chat.id, f'Country CODE : +383\n'
                                              f'ISO CODE : XK/XKX')
            enter(message)



        elif message.text == '383' or message.text == '+383':
            bot.send_message(message.chat.id, f'Country  : Kosovo\n'
                                              f'ISO CODE : XK/XKX')
            enter(message)

##############################################################################################################
# Kuwait                                    #
##############################################################################################################

        elif message.text == 'Kuwait' or message.text == 'kuwait':
            bot.send_message(message.chat.id, f'Country CODE : +965\n'
                                              f'ISO CODE : KW/KWT')
            enter(message)



        elif message.text == '965' or message.text == '+965':
            bot.send_message(message.chat.id, f'Country  : Kuwait\n'
                                              f'ISO CODE : KW/KWT')
            enter(message)


##############################################################################################################
# Kyrgyzstan                                    #
##############################################################################################################

        elif message.text == 'Kyrgyzstan' or message.text == 'kyrgyzstan':
            bot.send_message(message.chat.id, f'Country CODE : +996\n'
                                              f'ISO CODE : KG/KGZ')
            enter(message)



        elif message.text == '996' or message.text == '+996':
            bot.send_message(message.chat.id, f'Country  : Kyrgyzstan\n'
                                              f'ISO CODE : KG/KGZ')
            enter(message)


##############################################################################################################
# Laos                                    #
##############################################################################################################

        elif message.text == 'Laos' or message.text == 'laos':
            bot.send_message(message.chat.id, f'Country CODE : +856\n'
                                              f'ISO CODE : LA/LAO')
            enter(message)



        elif message.text == '856' or message.text == '+856':
            bot.send_message(message.chat.id, f'Country  : Laos\n'
                                              f'ISO CODE : LA/LAO')
            enter(message)


##############################################################################################################
# Latvia                                    #
##############################################################################################################

        elif message.text == 'Latvia' or message.text == 'latvia':
            bot.send_message(message.chat.id, f'Country CODE : +371\n'
                                              f'ISO CODE : LV/LVA')
            enter(message)



        elif message.text == '371' or message.text == '+371':
            bot.send_message(message.chat.id, f'Country  : Latvia\n'
                                              f'ISO CODE : LV/LVA')
            enter(message)


##############################################################################################################
# Lebanon                                    #
##############################################################################################################

        elif message.text == 'Lebanon' or message.text == 'lebanon':
            bot.send_message(message.chat.id, f'Country CODE : +961\n'
                                              f'ISO CODE : LB/LBN')
            enter(message)



        elif message.text == '961' or message.text == '+961':
            bot.send_message(message.chat.id, f'Country  : Lebanon\n'
                                              f'ISO CODE : LB/LBN')
            enter(message)


##############################################################################################################
# Lesotho                                    #
##############################################################################################################

        elif message.text == 'Lesotho' or message.text == 'lesotho':
            bot.send_message(message.chat.id, f'Country CODE : +266\n'
                                              f'ISO CODE : LS/LSO')
            enter(message)



        elif message.text == '266' or message.text == '+266':
            bot.send_message(message.chat.id, f'Country  : Lesotho\n'
                                              f'ISO CODE : LS/LSO')
            enter(message)

##############################################################################################################
# Liberia                                    #
##############################################################################################################

        elif message.text == 'Liberia' or message.text == 'liberia':
            bot.send_message(message.chat.id, f'Country CODE : +231\n'
                                              f'ISO CODE : LR/LBR')
            enter(message)



        elif message.text == '231' or message.text == '+231':
            bot.send_message(message.chat.id, f'Country  : Liberia\n'
                                              f'ISO CODE : LR/LBR')
            enter(message)


##############################################################################################################
# Libya                                    #
##############################################################################################################

        elif message.text == 'Libya' or message.text == 'libya':
            bot.send_message(message.chat.id, f'Country CODE : +218\n'
                                              f'ISO CODE : LY/LBY')
            enter(message)



        elif message.text == '218' or message.text == '+218':
            bot.send_message(message.chat.id, f'Country  : Libya\n'
                                              f'ISO CODE : LY/LBY')
            enter(message)


##############################################################################################################
# Libya                                    #
##############################################################################################################

        elif message.text == 'Liechtenstein' or message.text == 'liechtenstein':
            bot.send_message(message.chat.id, f'Country CODE : +423\n'
                                              f'ISO CODE : LI/LIE')
            enter(message)



        elif message.text == '423' or message.text == '+423':
            bot.send_message(message.chat.id, f'Country  : Liechtenstein\n'
                                              f'ISO CODE : LI/LIE')
            enter(message)


##############################################################################################################
# Lithuana                                    #
##############################################################################################################

        elif message.text == 'Lithuana' or message.text == 'lithuana':
            bot.send_message(message.chat.id, f'Country CODE : +370\n'
                                              f'ISO CODE : LT/LTU')
            enter(message)



        elif message.text == '370' or message.text == '+370':
            bot.send_message(message.chat.id, f'Country  : Lithuana\n'
                                              f'ISO CODE : LT/LTU')
            enter(message)


##############################################################################################################
# Luxembourg                                    #
##############################################################################################################

        elif message.text == 'Luxembourg' or message.text == 'luxembourg':
            bot.send_message(message.chat.id, f'Country CODE : +352\n'
                                              f'ISO CODE : LU/LUX')
            enter(message)



        elif message.text == '352' or message.text == '+352':
            bot.send_message(message.chat.id, f'Country  : Luxembourg\n'
                                              f'ISO CODE : LU/LUX')
            enter(message)


##############################################################################################################
# Macau                                    #
##############################################################################################################

        elif message.text == 'Macau' or message.text == 'Macau':
            bot.send_message(message.chat.id, f'Country CODE : +853\n'
                                              f'ISO CODE : MO/MAC')
            enter(message)



        elif message.text == '853' or message.text == '+853':
            bot.send_message(message.chat.id, f'Country  : Macau\n'
                                              f'ISO CODE : MO/MAC')
            enter(message)

##############################################################################################################
# Macedonia                                    #
##############################################################################################################

        elif message.text == 'Macedonia' or message.text == 'macedonia':
            bot.send_message(message.chat.id, f'Country CODE : +389\n'
                                              f'ISO CODE : MK/MKD')
            enter(message)



        elif message.text == '389' or message.text == '+389':
            bot.send_message(message.chat.id, f'Country  : Macedonia\n'
                                              f'ISO CODE : MK/MKD')
            enter(message)

##############################################################################################################
# Madagascar                                    #
##############################################################################################################

        elif message.text == 'Madagascar' or message.text == 'Madagascar':
            bot.send_message(message.chat.id, f'Country CODE : +261\n'
                                              f'ISO CODE : MG/MDG')
            enter(message)



        elif message.text == '261' or message.text == '+261':
            bot.send_message(message.chat.id, f'Country  : Madagascar\n'
                                              f'ISO CODE : MG/MDG')
            enter(message)


##############################################################################################################
# Malawi                                    #
##############################################################################################################

        elif message.text == 'Malawi' or message.text == 'malawi':
            bot.send_message(message.chat.id, f'Country CODE : +265\n'
                                              f'ISO CODE : MW/MWI')
            enter(message)



        elif message.text == '265' or message.text == '+265':
            bot.send_message(message.chat.id, f'Country  : Malawi\n'
                                              f'ISO CODE : MW/MWI')
            enter(message)


##############################################################################################################
# Malaysia                                   #
##############################################################################################################

        elif message.text == 'Malaysia' or message.text == 'malaysia':
            bot.send_message(message.chat.id, f'Country CODE : +60\n'
                                              f'ISO CODE : MY/MYS')
            enter(message)



        elif message.text == '60' or message.text == '+60':
            bot.send_message(message.chat.id, f'Country  : Malaysia\n'
                                              f'ISO CODE : MY/MYS')
            enter(message)

##############################################################################################################
# Maldives                                   #
##############################################################################################################

        elif message.text == 'Maldives' or message.text == 'maldives':
            bot.send_message(message.chat.id, f'Country CODE : +960\n'
                                              f'ISO CODE : MV/MDV')
            enter(message)



        elif message.text == '960' or message.text == '+960':
            bot.send_message(message.chat.id, f'Country  : Maldives\n'
                                              f'ISO CODE : MV/MDV')
            enter(message)


##############################################################################################################
# Mali                                   #
##############################################################################################################

        elif message.text == 'Mali' or message.text == 'mali':
            bot.send_message(message.chat.id, f'Country CODE : +223\n'
                                              f'ISO CODE : ML/MLI')
            enter(message)



        elif message.text == '223' or message.text == '+223':
            bot.send_message(message.chat.id, f'Country  : Mali\n'
                                              f'ISO CODE : ML/MLI')
            enter(message)


##############################################################################################################
# Mali                                   #
##############################################################################################################

        elif message.text == 'Malta' or message.text == 'malta':
            bot.send_message(message.chat.id, f'Country CODE : +356\n'
                                              f'ISO CODE : MT/MLT')
            enter(message)



        elif message.text == '356' or message.text == '+356':
            bot.send_message(message.chat.id, f'Country  : Malta\n'
                                              f'ISO CODE : MT/MLT')
            enter(message)


##############################################################################################################
# Mali                                   #
##############################################################################################################

        elif message.text == 'Marshall Islands' or message.text == 'Marshall islands' or message.text == 'marshall islands':
            bot.send_message(message.chat.id, f'Country CODE : +692\n'
                                              f'ISO CODE : MH/MHL')
            enter(message)



        elif message.text == '692' or message.text == '+692':
            bot.send_message(message.chat.id, f'Country  : Marshall Islands\n'
                                              f'ISO CODE : MT/MLT')
            enter(message)


##############################################################################################################
# Mauritania                                  #
##############################################################################################################

        elif message.text == 'Mauritania' or message.text == 'mauritania':
            bot.send_message(message.chat.id, f'Country CODE : +222\n'
                                              f'ISO CODE : MR/MRT')
            enter(message)



        elif message.text == '222' or message.text == '+222':
            bot.send_message(message.chat.id, f'Country  : Mauritania\n'
                                              f'ISO CODE : MR/MRT')
            enter(message)


##############################################################################################################
# Mauritius                                  #
##############################################################################################################

        elif message.text == 'Mauritius' or message.text == 'Mauritius':
            bot.send_message(message.chat.id, f'Country CODE : +230\n'
                                              f'ISO CODE : MU/MUS')
            enter(message)



        elif message.text == '230' or message.text == '+230':
            bot.send_message(message.chat.id, f'Country  : Mauritius\n'
                                              f'ISO CODE : MU/MUS')
            enter(message)



##############################################################################################################
# Mayotte                                 #
##############################################################################################################

        elif message.text == 'Mayotte' or message.text == 'mayotte':
            bot.send_message(message.chat.id, f'Country CODE : +262\n'
                                              f'ISO CODE : YT/MYT')
            enter(message)



        elif message.text == '262' or message.text == '+262':
            bot.send_message(message.chat.id, f'Country  : Mayotte\n'
                                              f'ISO CODE : YT/MYT')
            bot.send_message(message.chat.id, f'Country  : Reunion\n'
                                              f'ISO CODE : RE/REU')
            enter(message)


##############################################################################################################
# Mexico                                #
##############################################################################################################

        elif message.text == 'Mexico' or message.text == 'mexico':
            bot.send_message(message.chat.id, f'Country CODE : +52\n'
                                              f'ISO CODE : MX/MEX')
            enter(message)



        elif message.text == '52' or message.text == '+52':
            bot.send_message(message.chat.id, f'Country  : Mexico\n'
                                              f'ISO CODE : MX/MEX')
            enter(message)


##############################################################################################################
# Mexico                                #
##############################################################################################################

        elif message.text == 'Mexico' or message.text == 'mexico':
            bot.send_message(message.chat.id, f'Country CODE : +52\n'
                                              f'ISO CODE : MX/MEX')
            enter(message)



        elif message.text == '52' or message.text == '+52':
            bot.send_message(message.chat.id, f'Country  : Mexico\n'
                                              f'ISO CODE : MX/MEX')
            enter(message)

##############################################################################################################
# Micronesia                               #
##############################################################################################################

        elif message.text == 'Micronesia' or message.text == 'micronesia':
            bot.send_message(message.chat.id, f'Country CODE : +691\n'
                                              f'ISO CODE : FM/FSM')
            enter(message)



        elif message.text == '691' or message.text == '+691':
            bot.send_message(message.chat.id, f'Country  : Micronesia\n'
                                              f'ISO CODE : FM/FSM')
            enter(message)


##############################################################################################################
# Moldova                               #
##############################################################################################################

        elif message.text == 'Moldova' or message.text == 'moldova':
            bot.send_message(message.chat.id, f'Country CODE : +373\n'
                                              f'ISO CODE : MD/MDA')
            enter(message)



        elif message.text == '373' or message.text == '+373':
            bot.send_message(message.chat.id, f'Country  : Moldova\n'
                                              f'ISO CODE : MD/MDA')
            enter(message)


##############################################################################################################
# Monaco                              #
##############################################################################################################

        elif message.text == 'Monaco' or message.text == 'monaco':
            bot.send_message(message.chat.id, f'Country CODE : +377\n'
                                              f'ISO CODE : MC/MCO')
            enter(message)



        elif message.text == '377' or message.text == '+377':
            bot.send_message(message.chat.id, f'Country  : Monaco\n'
                                              f'ISO CODE : MC/MCO')
            enter(message)


##############################################################################################################
# Mongolia                             #
##############################################################################################################

        elif message.text == 'Mongolia' or message.text == 'mongolia':
            bot.send_message(message.chat.id, f'Country CODE : +976\n'
                                              f'ISO CODE : MN/MNG')
            enter(message)



        elif message.text == '976' or message.text == '+976':
            bot.send_message(message.chat.id, f'Country  : Mongolia\n'
                                              f'ISO CODE : MN/MNG')
            enter(message)

##############################################################################################################
# Montenegro                             #
##############################################################################################################

        elif message.text == 'Montenegro' or message.text == 'Montenegro':
            bot.send_message(message.chat.id, f'Country CODE : +382\n'
                                              f'ISO CODE : ME/MNE')
            enter(message)



        elif message.text == '382' or message.text == '+382':
            bot.send_message(message.chat.id, f'Country  : Montenegro\n'
                                              f'ISO CODE : ME/MNE')
            enter(message)


##############################################################################################################
# Montserrat                             #
##############################################################################################################

        elif message.text == 'Montserrat' or message.text == 'Montserrat':
            bot.send_message(message.chat.id, f'Country CODE : +1-664\n'
                                              f'ISO CODE : MS/MSR')
            enter(message)



        elif message.text == '1-664' or message.text == '+1-664':
            bot.send_message(message.chat.id, f'Country  : Montserrat\n'
                                              f'ISO CODE : ME/MNE')
            enter(message)


##############################################################################################################
# Morocco                             #
##############################################################################################################

        elif message.text == 'Morocco' or message.text == 'morocco':
            bot.send_message(message.chat.id, f'Country CODE : +212\n'
                                              f'ISO CODE : MA/MAR')
            enter(message)



        elif message.text == '212' or message.text == '+212':
            bot.send_message(message.chat.id, f'Country  : Morocco\n'
                                              f'ISO CODE : MA/MAR')
            bot.send_message(message.chat.id, f'Country  : Western Sahara\n'
                                              f'ISO CODE : EH/ESH')
            enter(message)


##############################################################################################################
# Mozambique                             #
##############################################################################################################

        elif message.text == 'Mozambique' or message.text == 'mozambique':
            bot.send_message(message.chat.id, f'Country CODE : +258\n'
                                              f'ISO CODE : MZ/MOZ')
            enter(message)



        elif message.text == '258' or message.text == '+258':
            bot.send_message(message.chat.id, f'Country  : Mozambique\n'
                                              f'ISO CODE : MZ/MOZ')
            enter(message)

##############################################################################################################
# Myanmar                             #
##############################################################################################################

        elif message.text == 'Myanmar' or message.text == 'Myanmar':
            bot.send_message(message.chat.id, f'Country CODE : +95\n'
                                              f'ISO CODE : MM/MMR')
            enter(message)



        elif message.text == '95' or message.text == '+95':
            bot.send_message(message.chat.id, f'Country  : Myanmar\n'
                                              f'ISO CODE : MM/MMR')
            enter(message)


##############################################################################################################
# Namibia                             #
##############################################################################################################

        elif message.text == 'Namibia' or message.text == 'Namibia':
            bot.send_message(message.chat.id, f'Country CODE : +264\n'
                                              f'ISO CODE : NA/NAM')
            enter(message)



        elif message.text == '264' or message.text == '+264':
            bot.send_message(message.chat.id, f'Country  : Namibia\n'
                                              f'ISO CODE : NA/NAM')
            enter(message)


##############################################################################################################
# Nauru                            #
##############################################################################################################

        elif message.text == 'Nauru' or message.text == 'nauru':
            bot.send_message(message.chat.id, f'Country CODE : +674\n'
                                              f'ISO CODE : NR/NRU')
            enter(message)



        elif message.text == '674' or message.text == '+674':
            bot.send_message(message.chat.id, f'Country  : Nauru\n'
                                              f'ISO CODE : NR/NRU')
            enter(message)


##############################################################################################################
# Nepal                            #
##############################################################################################################

        elif message.text == 'Nepal' or message.text == 'Nepal':
            bot.send_message(message.chat.id, f'Country CODE : +977\n'
                                              f'ISO CODE : NP/NPL')
            enter(message)



        elif message.text == '977' or message.text == '+977':
            bot.send_message(message.chat.id, f'Country  : Nepal\n'
                                              f'ISO CODE : NP/NPL')
            enter(message)

##############################################################################################################
# Netherlands                           #
##############################################################################################################

        elif message.text == 'Netherlands' or message.text == 'Netherlands':
            bot.send_message(message.chat.id, f'Country CODE : +31\n'
                                              f'ISO CODE : NL/NLD')
            enter(message)



        elif message.text == '31' or message.text == '+31':
            bot.send_message(message.chat.id, f'Country  : Netherlands\n'
                                              f'ISO CODE : NL/NLD')
            enter(message)


##############################################################################################################
# Netherlands Antilles                           #
##############################################################################################################

        elif message.text == 'Netherlands Antilles' or message.text == 'Netherlands antilles' or message.text == 'netherlands antilles':
            bot.send_message(message.chat.id, f'Country CODE : +599\n'
                                              f'ISO CODE : AN/ANT')
            enter(message)

##############################################################################################################
# New Caledonia                           #
##############################################################################################################

        elif message.text == 'New Caledonia' or message.text == 'New caledonia' or message.text == 'new caledonia':
            bot.send_message(message.chat.id, f'Country CODE : +687\n'
                                              f'ISO CODE : NC/NCL')
            enter(message)



        elif message.text == '687' or message.text == '+687':
            bot.send_message(message.chat.id, f'Country  : New Caledonia\n'
                                              f'ISO CODE : NC/NCL')
            enter(message)


##############################################################################################################
# New Caledonia                           #
##############################################################################################################

        elif message.text == 'New Caledonia' or message.text == 'New caledonia' or message.text == 'new caledonia':
            bot.send_message(message.chat.id, f'Country CODE : +687\n'
                                              f'ISO CODE : NC/NCL')
            enter(message)



        elif message.text == '687' or message.text == '+687':
            bot.send_message(message.chat.id, f'Country  : New Caledonia\n'
                                              f'ISO CODE : NC/NCL')
            enter(message)

##############################################################################################################
# New Zealand                           #
##############################################################################################################

        elif message.text == 'New Zealand' or message.text == 'New zealand' or message.text == 'new zealand':
            bot.send_message(message.chat.id, f'Country CODE : +64\n'
                                              f'ISO CODE : NZ/NZL')
            enter(message)



        elif message.text == '64' or message.text == '+64':
            bot.send_message(message.chat.id, f'Country  : New Zealand\n'
                                              f'ISO CODE : NZ/NZL')
            enter(message)


##############################################################################################################
# Nicaragua                          #
##############################################################################################################

        elif message.text == 'Nicaragua' or message.text == 'nicaragua':
            bot.send_message(message.chat.id, f'Country CODE : +505\n'
                                              f'ISO CODE : NI/NIC')
            enter(message)



        elif message.text == '505' or message.text == '+505':
            bot.send_message(message.chat.id, f'Country  : Nicaragua\n'
                                              f'ISO CODE : NI/NIC')
            enter(message)


##############################################################################################################
# Niger                        #
##############################################################################################################

        elif message.text == 'Niger' or message.text == 'niger':
            bot.send_message(message.chat.id, f'Country CODE : +227\n'
                                              f'ISO CODE : NE/NER')
            enter(message)



        elif message.text == '227' or message.text == '+227':
            bot.send_message(message.chat.id, f'Country  : Niger\n'
                                              f'ISO CODE : NE/NER')
            enter(message)


##############################################################################################################
# Nigeria                        #
##############################################################################################################

        elif message.text == 'Nigeria' or message.text == 'nigeria':
            bot.send_message(message.chat.id, f'Country CODE : +234\n'
                                              f'ISO CODE : NG/NGA')
            enter(message)



        elif message.text == '234' or message.text == '+234':
            bot.send_message(message.chat.id, f'Country  : Nigeria\n'
                                              f'ISO CODE : NG/NGA')
            enter(message)



##############################################################################################################
# Niue                        #
##############################################################################################################

        elif message.text == 'Niue' or message.text == 'niue':
            bot.send_message(message.chat.id, f'Country CODE : +683\n'
                                              f'ISO CODE : NU/NIU')
            enter(message)



        elif message.text == '683' or message.text == '+683':
            bot.send_message(message.chat.id, f'Country  : Niue\n'
                                              f'ISO CODE : NG/NGA')
            enter(message)


##############################################################################################################
# North Korea                       #
##############################################################################################################

        elif message.text == 'North Korea' or message.text == 'North korea' or message.text == 'north korea':
            bot.send_message(message.chat.id, f'Country CODE : +850\n'
                                              f'ISO CODE : KP/PRK')
            enter(message)



        elif message.text == '850' or message.text == '+850':
            bot.send_message(message.chat.id, f'Country  : North Korea\n'
                                              f'ISO CODE : KP/PRK')
            enter(message)


##############################################################################################################
# Northern Marina Islands                      #
##############################################################################################################

        elif message.text == 'Northern Marina Islands' or message.text == 'Northern marina islands' or message.text == 'northern marina islands':
            bot.send_message(message.chat.id, f'Country CODE : +1-670\n'
                                              f'ISO CODE : MP/MNP')
            enter(message)



        elif message.text == '1-670' or message.text == '+1-670':
            bot.send_message(message.chat.id, f'Country  : Northern Marina Islands\n'
                                              f'ISO CODE : MP/MNP')
            enter(message)


##############################################################################################################
# Norway                       #
##############################################################################################################

        elif message.text == 'Norway' or message.text == 'norway':
            bot.send_message(message.chat.id, f'Country CODE : +47\n'
                                              f'ISO CODE : NO/NOR')
            enter(message)



        elif message.text == '47' or message.text == '+47':
            bot.send_message(message.chat.id, f'Country  : Norway\n'
                                              f'ISO CODE : NO/NOR')
            bot.send_message(message.chat.id, f'Country  : Svalbard and Jan Mayen\n'
                                              f'ISO CODE : SJ/SJM')
            enter(message)


##############################################################################################################
# Oman                       #
##############################################################################################################

        elif message.text == 'Oman' or message.text == 'oman':
            bot.send_message(message.chat.id, f'Country CODE : +968\n'
                                              f'ISO CODE : OM/OMN')
            enter(message)



        elif message.text == '968' or message.text == '+968':
            bot.send_message(message.chat.id, f'Country  : Oman\n'
                                              f'ISO CODE : OM/OMN')
            enter(message)


##############################################################################################################
# Pakistan                      #
##############################################################################################################

        elif message.text == 'Pakistan' or message.text == 'pakistan':
            bot.send_message(message.chat.id, f'Country CODE : +92\n'
                                              f'ISO CODE : PK/PAK')
            enter(message)



        elif message.text == '92' or message.text == '+92':
            bot.send_message(message.chat.id, f'Country  : Pakistan\n'
                                              f'ISO CODE : PK/PAK')
            enter(message)


##############################################################################################################
# Palau                     #
##############################################################################################################

        elif message.text == 'Palau' or message.text == 'palau':
            bot.send_message(message.chat.id, f'Country CODE : +680\n'
                                              f'ISO CODE : PW/PLW')
            enter(message)



        elif message.text == '680' or message.text == '+680':
            bot.send_message(message.chat.id, f'Country  : palau\n'
                                              f'ISO CODE : PW/PLW')
            enter(message)


##############################################################################################################
# Palau                     #
##############################################################################################################

        elif message.text == 'Palau' or message.text == 'palau':
            bot.send_message(message.chat.id, f'Country CODE : +680\n'
                                              f'ISO CODE : PW/PLW')
            enter(message)



        elif message.text == '680' or message.text == '+680':
            bot.send_message(message.chat.id, f'Country  : palau\n'
                                              f'ISO CODE : PW/PLW')
            enter(message)


##############################################################################################################
# Palestine                     #
##############################################################################################################

        elif message.text == 'Palestine' or message.text == 'palestine':
            bot.send_message(message.chat.id, f'Country CODE : +970\n'
                                              f'ISO CODE : PS/PSE')
            enter(message)



        elif message.text == '970' or message.text == '+970':
            bot.send_message(message.chat.id, f'Country  : Palestine\n'
                                              f'ISO CODE : PS/PSE')
            enter(message)


##############################################################################################################
# Panama                     #
##############################################################################################################

        elif message.text == 'Panamae' or message.text == 'Panama':
            bot.send_message(message.chat.id, f'Country CODE : +507\n'
                                              f'ISO CODE : PA/PAN')
            enter(message)



        elif message.text == '507' or message.text == '+507':
            bot.send_message(message.chat.id, f'Country  : Panama\n'
                                              f'ISO CODE : PA/PAN')
            enter(message)


##############################################################################################################
# Papua New Guinea                     #
##############################################################################################################

        elif message.text == 'Papua New Guinea' or message.text == 'Papua new guinea' or message.text == 'papua new guinea':
            bot.send_message(message.chat.id, f'Country CODE : +675\n'
                                              f'ISO CODE : PG/PNG')
            enter(message)



        elif message.text == '675' or message.text == '+675':
            bot.send_message(message.chat.id, f'Country  : Papua New Guinea\n'
                                              f'ISO CODE : PG/PNG')
            enter(message)

##############################################################################################################
# Paraguay                     #
##############################################################################################################

        elif message.text == 'Paraguay' or message.text == 'paraguay':
            bot.send_message(message.chat.id, f'Country CODE : +595\n'
                                              f'ISO CODE : PY/PRY')
            enter(message)



        elif message.text == '595' or message.text == '+595':
            bot.send_message(message.chat.id, f'Country  : Paraguay\n'
                                              f'ISO CODE : PA/PAN')
            enter(message)


##############################################################################################################
# Peru                    #
##############################################################################################################

        elif message.text == 'Peru' or message.text == 'Peru':
            bot.send_message(message.chat.id, f'Country CODE : +51\n'
                                              f'ISO CODE : PE/PER')
            enter(message)



        elif message.text == '51' or message.text == '+51':
            bot.send_message(message.chat.id, f'Country  : Peru\n'
                                              f'ISO CODE : PE/PER')
            enter(message)


##############################################################################################################
# Philippines                    #
##############################################################################################################

        elif message.text == 'Philippines' or message.text == 'Philippines':
            bot.send_message(message.chat.id, f'Country CODE : +63\n'
                                              f'ISO CODE : PH/PHL')
            enter(message)



        elif message.text == '63' or message.text == '+63':
            bot.send_message(message.chat.id, f'Country  : Philippines\n'
                                              f'ISO CODE : PH/PHL')
            enter(message)


##############################################################################################################
# Pitcairn                    #
##############################################################################################################

        elif message.text == 'Pitcairn' or message.text == 'Pitcairn':
            bot.send_message(message.chat.id, f'Country CODE : +64\n'
                                              f'ISO CODE : PN/PCN')
            enter(message)



        elif message.text == '64' or message.text == '+64':
            bot.send_message(message.chat.id, f'Country  : pitcairn\n'
                                              f'ISO CODE : PN/PCN')
            enter(message)


##############################################################################################################
# Poland                    #
##############################################################################################################

        elif message.text == 'Poland' or message.text == 'Poland':
            bot.send_message(message.chat.id, f'Country CODE : +48\n'
                                              f'ISO CODE : PL/POL')
            enter(message)



        elif message.text == '48' or message.text == '+48':
            bot.send_message(message.chat.id, f'Country  : Poland\n'
                                              f'ISO CODE : PL/POL')
            enter(message)


##############################################################################################################
# Portugal                    #
##############################################################################################################

        elif message.text == 'Portugal' or message.text == 'portugal':
            bot.send_message(message.chat.id, f'Country CODE : +351\n'
                                              f'ISO CODE : PT/PRT')
            enter(message)



        elif message.text == '351' or message.text == '+351':
            bot.send_message(message.chat.id, f'Country  : Portugal\n'
                                              f'ISO CODE : PT/PRT')
            enter(message)

##############################################################################################################
# Puerto Rico                    #
##############################################################################################################

        elif message.text == 'Puerto Rico' or message.text == 'Puerto rico' or message.text == 'puerto rico':
            bot.send_message(message.chat.id, f'Country CODE : +1-787, +1-939\n'
                                              f'ISO CODE : PR/PRI')
            enter(message)



        elif message.text == '1-787' or message.text == '+1-787' or message.text == '1-939' or message.text == '+1-939':
            bot.send_message(message.chat.id, f'Country  : Puerto Rico\n'
                                              f'ISO CODE : PR/PRI')
            enter(message)


##############################################################################################################
# Qatar                   #
##############################################################################################################

        elif message.text == 'Qatar' or message.text == 'qatar':
            bot.send_message(message.chat.id, f'Country CODE : +974\n'
                                              f'ISO CODE : QA/QAT')
            enter(message)



        elif message.text == '974' or message.text == '+974':
            bot.send_message(message.chat.id, f'Country  : Qatar\n'
                                              f'ISO CODE : QA/QAT')
            enter(message)


##############################################################################################################
# Republic of the Congo                   #
##############################################################################################################

        elif message.text == 'Republic of the Congo' or message.text == 'Republic of the congo' or message.text == 'republic of the congo':
            bot.send_message(message.chat.id, f'Country CODE : +242\n'
                                              f'ISO CODE : CG/COG')
            enter(message)



        elif message.text == '242' or message.text == '+242':
            bot.send_message(message.chat.id, f'Country  : Republic of the Congo\n'
                                              f'ISO CODE : CG/COG')
            enter(message)


##############################################################################################################
# Reunion                   #
##############################################################################################################

        elif message.text == 'Reunion' or message.text == 'reunion':
            bot.send_message(message.chat.id, f'Country CODE : +262\n'
                                              f'ISO CODE : RE/REU')
            enter(message)


##############################################################################################################
# Romania                   #
##############################################################################################################

        elif message.text == 'Romania' or message.text == 'romania':
            bot.send_message(message.chat.id, f'Country CODE : +40\n'
                                              f'ISO CODE : RO/ROU')
            enter(message)



        elif message.text == '40' or message.text == '+40':
            bot.send_message(message.chat.id, f'Country  : Romania\n'
                                              f'ISO CODE : RO/ROU')
            enter(message)


##############################################################################################################
# Russia                   #
##############################################################################################################

        elif message.text == 'Russia' or message.text == 'russia':
            bot.send_message(message.chat.id, f'Country CODE : +7\n'
                                              f'ISO CODE : RU/RUS')
            enter(message)


##############################################################################################################
# Rwanda                   #
##############################################################################################################

        elif message.text == 'Rwanda' or message.text == 'rwanda':
            bot.send_message(message.chat.id, f'Country CODE : +250\n'
                                              f'ISO CODE : RW/RWA')
            enter(message)



        elif message.text == '250' or message.text == '+250':
            bot.send_message(message.chat.id, f'Country  : Rwanda\n'
                                              f'ISO CODE : RW/RWA')
            enter(message)


##############################################################################################################
# Saint Barthelemy                   #
##############################################################################################################

        elif message.text == 'Saint Barthelemy' or message.text == 'Saint barthelemy' or message.text == 'saint barthelemy':
            bot.send_message(message.chat.id, f'Country CODE : +590\n'
                                              f'ISO CODE : BL/BLM')
            enter(message)



        elif message.text == '590' or message.text == '+590':
            bot.send_message(message.chat.id, f'Country  : Saint Barthelemy\n'
                                              f'ISO CODE : BL/BLM')
            bot.send_message(message.chat.id, f'Country  : Saint Martin\n'
                                              f'ISO CODE : MF/MAF')
            enter(message)

##############################################################################################################
# Saint Helena                   #
##############################################################################################################

        elif message.text == 'Saint Helena' or message.text == 'Saint helena' or message.text == 'saint helena':
            bot.send_message(message.chat.id, f'Country CODE : +290\n'
                                              f'ISO CODE : SH/SHN')
            enter(message)



        elif message.text == '290' or message.text == '+290':
            bot.send_message(message.chat.id, f'Country  : Saint Helena\n'
                                              f'ISO CODE : SH/SHN')
            enter(message)


##############################################################################################################
# Saint Kitts and Nevis                  #
##############################################################################################################

        elif message.text == 'Saint Kitts and Nevis' or message.text == 'Saint kitts and nevis' or message.text == 'saint kitts and nevis':
            bot.send_message(message.chat.id, f'Country CODE : +1-869\n'
                                              f'ISO CODE : KN/KNA')
            enter(message)



        elif message.text == '1-869' or message.text == '+1-869':
            bot.send_message(message.chat.id, f'Country  : Saint Kitts and Nevis\n'
                                              f'ISO CODE : KN/KNA')
            enter(message)

##############################################################################################################
# Saint Lucia                  #
##############################################################################################################

        elif message.text == 'Saint Lucia' or message.text == 'Saint lucia' or message.text == 'saint lucia':
            bot.send_message(message.chat.id, f'Country CODE : +1-758\n'
                                              f'ISO CODE : LC/LCA')
            enter(message)



        elif message.text == '1-758' or message.text == '+1-758':
            bot.send_message(message.chat.id, f'Country  : Saint Lucia\n'
                                              f'ISO CODE : LC/LCA')
            enter(message)


##############################################################################################################
# Saint Martin                  #
##############################################################################################################

        elif message.text == 'Saint Martin' or message.text == 'Saint Martin' or message.text == 'saint martin':
            bot.send_message(message.chat.id, f'Country CODE : +590\n'
                                              f'ISO CODE : MF/MAF')
            enter(message)


##############################################################################################################
# Saint Pierre and miquelon                 #
##############################################################################################################

        elif message.text == 'Saint Pierre and Miquelon' or message.text == 'Saint pierre and miquelon' or message.text == 'saint pierre and miquelon':
            bot.send_message(message.chat.id, f'Country CODE : +508\n'
                                              f'ISO CODE : PM/SPM')
            enter(message)



        elif message.text == '508' or message.text == '+508':
            bot.send_message(message.chat.id, f'Country  : Saint Lucia\n'
                                              f'ISO CODE : PM/SPM')
            enter(message)


##############################################################################################################
# Saint Vincent and the Grenadines                 #
##############################################################################################################

        elif message.text == 'Saint Vincent and the Grenadines' or message.text == 'Saint vincent and the grenadines' or message.text == 'saint vincent and the grenadines':
            bot.send_message(message.chat.id, f'Country CODE : +1-784\n'
                                              f'ISO CODE : VC/VCT')
            enter(message)



        elif message.text == '1-784' or message.text == '+1-784':
            bot.send_message(message.chat.id, f'Country  : Saint Vincent and the Grenadines\n'
                                              f'ISO CODE : VC/VCT')
            enter(message)


##############################################################################################################
# Samoa                 #
##############################################################################################################

        elif message.text == 'Samoa' or message.text == 'samoa':
            bot.send_message(message.chat.id, f'Country CODE : +685\n'
                                              f'ISO CODE : WS/WSM')
            enter(message)



        elif message.text == '685' or message.text == '+685':
            bot.send_message(message.chat.id, f'Country  : Samoa\n'
                                              f'ISO CODE : WS/WSM')
            enter(message)



##############################################################################################################
# San Marino                  #
##############################################################################################################

        elif message.text == 'San Marino' or message.text == 'San marino' or message.text == 'san marino':
            bot.send_message(message.chat.id, f'Country CODE : +378\n'
                                              f'ISO CODE : SM/SMR')
            enter(message)



        elif message.text == '378' or message.text == '+378':
            bot.send_message(message.chat.id, f'Country  : San Marino\n'
                                              f'ISO CODE : SM/SMR')
            enter(message)


##############################################################################################################
# Sao Tome and Principe                  #
##############################################################################################################

        elif message.text == 'Sao Tome and Principe' or message.text == 'Sao tome and principe' or message.text == 'sao tome and principe':
            bot.send_message(message.chat.id, f'Country CODE : +239\n'
                                              f'ISO CODE : ST/STP')
            enter(message)



        elif message.text == '239' or message.text == '+239':
            bot.send_message(message.chat.id, f'Country  : Sao Tome and Principe\n'
                                              f'ISO CODE : ST/STP')
            enter(message)




##############################################################################################################
# Saudi Arabia                  #
##############################################################################################################

        elif message.text == 'Saudi Arabia' or message.text == 'Saudi arabia' or message.text == 'saudi arabia':
            bot.send_message(message.chat.id, f'Country CODE : +966\n'
                                              f'ISO CODE : SA/SAU')
            enter(message)



        elif message.text == '966' or message.text == '+966':
            bot.send_message(message.chat.id, f'Country  : Saudi Arabia\n'
                                              f'ISO CODE : SA/SAU')
            enter(message)


##############################################################################################################
# Senegal                  #
##############################################################################################################

        elif message.text == 'Senegal' or message.text == 'senegal':
            bot.send_message(message.chat.id, f'Country CODE : +221\n'
                                              f'ISO CODE : SN/SEN')
            enter(message)



        elif message.text == '221' or message.text == '+221':
            bot.send_message(message.chat.id, f'Country  : Senegal\n'
                                              f'ISO CODE : SN/SEN')
            enter(message)

##############################################################################################################
# Serbia                  #
##############################################################################################################

        elif message.text == 'Serbia' or message.text == 'serbia':
            bot.send_message(message.chat.id, f'Country CODE : +381\n'
                                              f'ISO CODE : RS/SRB')
            enter(message)



        elif message.text == '381' or message.text == '+381':
            bot.send_message(message.chat.id, f'Country  : Serbia\n'
                                              f'ISO CODE : SN/SEN')
            enter(message)

##############################################################################################################
# Seychelles                 #
##############################################################################################################

        elif message.text == 'Seychelles' or message.text == 'seychelles':
            bot.send_message(message.chat.id, f'Country CODE : +248\n'
                                              f'ISO CODE : SC/SYC')
            enter(message)



        elif message.text == '248' or message.text == '+248':
            bot.send_message(message.chat.id, f'Country  : Seychelles\n'
                                              f'ISO CODE : SC/SYC')
            enter(message)


##############################################################################################################
# Sierra Leone                 #
##############################################################################################################

        elif message.text == 'Sierra Leone' or message.text == 'Sierra leone' or message.text == 'sierra leone':
            bot.send_message(message.chat.id, f'Country CODE : +232\n'
                                              f'ISO CODE : SL/SLE')
            enter(message)



        elif message.text == '232' or message.text == '+232':
            bot.send_message(message.chat.id, f'Country  : Sierra Leone\n'
                                              f'ISO CODE : SL/SLE')
            enter(message)


##############################################################################################################
# Singapore                 #
##############################################################################################################

        elif message.text == 'Singapore' or message.text == 'singapore':
            bot.send_message(message.chat.id, f'Country CODE : +65\n'
                                              f'ISO CODE : SG/SGP')
            enter(message)



        elif message.text == '65' or message.text == '+65':
            bot.send_message(message.chat.id, f'Country  : Singapore\n'
                                              f'ISO CODE : SG/SGP')
            enter(message)

##############################################################################################################
# Sint Maarten                 #
##############################################################################################################

        elif message.text == 'Sint Maarten' or message.text == 'Sint maarten' or message.text == 'sint maarten':
            bot.send_message(message.chat.id, f'Country CODE : +1-721\n'
                                              f'ISO CODE : SX/SXM')
            enter(message)



        elif message.text == '1-721' or message.text == '+1-721':
            bot.send_message(message.chat.id, f'Country  : Sint Maarten\n'
                                              f'ISO CODE : SX/SXM')
            enter(message)


##############################################################################################################
# Slovakia                 #
##############################################################################################################

        elif message.text == 'Slovakia' or message.text == 'Slovakia':
            bot.send_message(message.chat.id, f'Country CODE : +421\n'
                                              f'ISO CODE : SK/SVK')
            enter(message)



        elif message.text == '421' or message.text == '+421':
            bot.send_message(message.chat.id, f'Country  : Slovakia\n'
                                              f'ISO CODE : SK/SVK')
            enter(message)

##############################################################################################################
# Slovenia                 #
##############################################################################################################

        elif message.text == 'Slovenia' or message.text == 'slovenia':
            bot.send_message(message.chat.id, f'Country CODE : +386\n'
                                              f'ISO CODE : SL/SVN')
            enter(message)



        elif message.text == '386' or message.text == '+386':
            bot.send_message(message.chat.id, f'Country  : Slovenia\n'
                                              f'ISO CODE : SL/SVN')
            enter(message)


##############################################################################################################
# Solomon Islands                 #
##############################################################################################################

        elif message.text == 'Solomon Islands' or message.text == 'Solomon Islands' or message.text == 'solomon islands':
            bot.send_message(message.chat.id, f'Country CODE : +677\n'
                                              f'ISO CODE : SB/SLB')
            enter(message)



        elif message.text == '677' or message.text == '+677':
            bot.send_message(message.chat.id, f'Country  : Solomon Islands\n'
                                              f'ISO CODE : SB/SLB')
            enter(message)


##############################################################################################################
# Somalia               #
##############################################################################################################

        elif message.text == 'Somalia' or message.text == 'somalia':
            bot.send_message(message.chat.id, f'Country CODE : +252\n'
                                              f'ISO CODE : SO/SOM')
            enter(message)



        elif message.text == '252' or message.text == '+252':
            bot.send_message(message.chat.id, f'Country  : Somalia\n'
                                              f'ISO CODE : SO/SOM')
            enter(message)

##############################################################################################################
# South Africa              #
##############################################################################################################

        elif message.text == 'South Africa' or message.text == 'South africa' or message.text == 'south africa':
            bot.send_message(message.chat.id, f'Country CODE : +27\n'
                                              f'ISO CODE : ZA/ZAF')
            enter(message)



        elif message.text == '27' or message.text == '+27':
            bot.send_message(message.chat.id, f'Country  : South Africa\n'
                                              f'ISO CODE : ZA/ZAF')
            enter(message)


##############################################################################################################
# South Korea              #
##############################################################################################################

        elif message.text == 'South Korea' or message.text == 'South korea' or message.text == 'south korea':
            bot.send_message(message.chat.id, f'Country CODE : +82\n'
                                              f'ISO CODE : KR/KOR')
            enter(message)



        elif message.text == '82' or message.text == '+82':
            bot.send_message(message.chat.id, f'Country  : South Korea\n'
                                              f'ISO CODE : KR/KOR')
            enter(message)

##############################################################################################################
# South Sudan              #
##############################################################################################################

        elif message.text == 'South Sudan' or message.text == 'South sudan' or message.text == 'south sudan':
            bot.send_message(message.chat.id, f'Country CODE : +211\n'
                                              f'ISO CODE : SS/SSD')
            enter(message)



        elif message.text == '211' or message.text == '+211':
            bot.send_message(message.chat.id, f'Country  : South Sudan\n'
                                              f'ISO CODE : SS/SSD')
            enter(message)



##############################################################################################################
# Spain              #
##############################################################################################################

        elif message.text == 'Spain' or message.text == 'spain':
            bot.send_message(message.chat.id, f'Country CODE : +34\n'
                                              f'ISO CODE : ES/ESP')
            enter(message)



        elif message.text == '34' or message.text == '+34':
            bot.send_message(message.chat.id, f'Country  : Spain\n'
                                              f'ISO CODE : SO/SOM')
            enter(message)


##############################################################################################################
# Sri Lanka             #
##############################################################################################################

        elif message.text == 'Sri Lanka' or message.text == 'Sri lanka' or message.text == 'sri lanka':
            bot.send_message(message.chat.id, f'Country CODE : +94\n'
                                              f'ISO CODE : LK/LKA')
            enter(message)



        elif message.text == '94' or message.text == '+94':
            bot.send_message(message.chat.id, f'Country  : Sri Lanka\n'
                                              f'ISO CODE : LK/LKA')
            enter(message)


##############################################################################################################
# Sudan              #
##############################################################################################################

        elif message.text == 'Sudan' or message.text == 'sudan':
            bot.send_message(message.chat.id, f'Country CODE : +249\n'
                                              f'ISO CODE : SD/SDN')
            enter(message)



        elif message.text == '249' or message.text == '+249':
            bot.send_message(message.chat.id, f'Country  : Sudan\n'
                                              f'ISO CODE : SD/SDN')
            enter(message)

##############################################################################################################
# Suriname              #
##############################################################################################################

        elif message.text == 'Suriname' or message.text == 'suriname':
            bot.send_message(message.chat.id, f'Country CODE : +597\n'
                                              f'ISO CODE : SR/SUR')
            enter(message)



        elif message.text == '597' or message.text == '+597':
            bot.send_message(message.chat.id, f'Country  : Suriname\n'
                                              f'ISO CODE : SR/SUR')
            enter(message)


##############################################################################################################
# Svalbard and Jan Mayen              #
##############################################################################################################

        elif message.text == 'Svalbard and Jan Mayen' or message.text == 'Svalbard and jan mayen' or message.text == 'svalbard and jan mayen':
            bot.send_message(message.chat.id, f'Country CODE : +47\n'
                                              f'ISO CODE : SJ/SJM')
            enter(message)

##############################################################################################################
# Swaziland              #
##############################################################################################################

        elif message.text == 'Swaziland' or message.text == 'swaziland':
            bot.send_message(message.chat.id, f'Country CODE : +268\n'
                                              f'ISO CODE : SZ/SWZ')
            enter(message)



        elif message.text == '597' or message.text == '+597':
            bot.send_message(message.chat.id, f'Country  : Swaziland\n'
                                              f'ISO CODE : SZ/SWZ')
            enter(message)


##############################################################################################################
# Sweden              #
##############################################################################################################

        elif message.text == 'Sweden' or message.text == 'sweden':
            bot.send_message(message.chat.id, f'Country CODE : +46\n'
                                              f'ISO CODE : SE/SWE')
            enter(message)



        elif message.text == '46' or message.text == '+46':
            bot.send_message(message.chat.id, f'Country  : Sweden\n'
                                              f'ISO CODE : SZ/SWZ')
            enter(message)


##############################################################################################################
# Switzerland              #
##############################################################################################################

        elif message.text == 'Switzerland' or message.text == 'switzerland':
            bot.send_message(message.chat.id, f'Country CODE : +41\n'
                                              f'ISO CODE : CH/CHE')
            enter(message)



        elif message.text == '41' or message.text == '+41':
            bot.send_message(message.chat.id, f'Country  : Switzerland\n'
                                              f'ISO CODE : CH/CHE')
            enter(message)

##############################################################################################################
# Syria              #
##############################################################################################################

        elif message.text == 'Syria' or message.text == 'syria':
            bot.send_message(message.chat.id, f'Country CODE : +963\n'
                                              f'ISO CODE : SY/SYR')
            enter(message)



        elif message.text == '963' or message.text == '+963':
            bot.send_message(message.chat.id, f'Country  : Syria\n'
                                              f'ISO CODE : SY/SYR')
            enter(message)



##############################################################################################################
# Taiwan              #
##############################################################################################################

        elif message.text == 'Taiwan' or message.text == 'Taiwan':
            bot.send_message(message.chat.id, f'Country CODE : +886\n'
                                              f'ISO CODE : TW/TWN')
            enter(message)



        elif message.text == '886' or message.text == '+886':
            bot.send_message(message.chat.id, f'Country  : Taiwan\n'
                                              f'ISO CODE : TW/TWN')
            enter(message)


##############################################################################################################
# Tajikistan             #
##############################################################################################################

        elif message.text == 'Tajikistan' or message.text == 'Tajikistan':
            bot.send_message(message.chat.id, f'Country CODE : +992\n'
                                              f'ISO CODE : TJ/TJK')
            enter(message)



        elif message.text == '992' or message.text == '+992':
            bot.send_message(message.chat.id, f'Country  : Tajikistan\n'
                                              f'ISO CODE : TJ/TJK')
            enter(message)

##############################################################################################################
# Tanzania             #
##############################################################################################################

        elif message.text == 'Tanzania' or message.text == 'Tanzania':
            bot.send_message(message.chat.id, f'Country CODE : +255\n'
                                              f'ISO CODE : TZ/TZA')
            enter(message)



        elif message.text == '255' or message.text == '+255':
            bot.send_message(message.chat.id, f'Country  : Tanzania\n'
                                              f'ISO CODE : TZ/TZA')
            enter(message)


##############################################################################################################
# Thailand             #
##############################################################################################################

        elif message.text == 'Thailand' or message.text == 'thailand':
            bot.send_message(message.chat.id, f'Country CODE : +66\n'
                                              f'ISO CODE : TH/THA')
            enter(message)



        elif message.text == '66' or message.text == '+66':
            bot.send_message(message.chat.id, f'Country  : Thailand\n'
                                              f'ISO CODE : TH/THA')
            enter(message)


##############################################################################################################
# Togo            #
##############################################################################################################

        elif message.text == 'Togo' or message.text == 'togo':
            bot.send_message(message.chat.id, f'Country CODE : +228\n'
                                              f'ISO CODE : TG/TGO')
            enter(message)



        elif message.text == '228' or message.text == '+228':
            bot.send_message(message.chat.id, f'Country  : Togo\n'
                                              f'ISO CODE : TG/TGO')
            enter(message)

##############################################################################################################
# Tokelau            #
##############################################################################################################

        elif message.text == 'Tokelau' or message.text == 'tokelau':
            bot.send_message(message.chat.id, f'Country CODE : +690\n'
                                              f'ISO CODE : TK/TKL')
            enter(message)



        elif message.text == '690' or message.text == '+690':
            bot.send_message(message.chat.id, f'Country  : Tokelau\n'
                                              f'ISO CODE : TK/TKL')
            enter(message)


##############################################################################################################
# Tonga            #
##############################################################################################################

        elif message.text == 'Tonga' or message.text == 'tonga':
            bot.send_message(message.chat.id, f'Country CODE : +676\n'
                                              f'ISO CODE : TO/TON')
            enter(message)



        elif message.text == '676' or message.text == '+676':
            bot.send_message(message.chat.id, f'Country  : Tonga\n'
                                              f'ISO CODE : TO/TON')
            enter(message)


##############################################################################################################
# Trinidad and Tobago           #
##############################################################################################################

        elif message.text == 'Trinidad and Tobago' or message.text == 'Trinidad and tobago' or message.text == 'trinidad and tobago':
            bot.send_message(message.chat.id, f'Country CODE : +1-868\n'
                                              f'ISO CODE : TT/TTO')
            enter(message)



        elif message.text == '1-868' or message.text == '+1-868':
            bot.send_message(message.chat.id, f'Country  : Trinidad and Tobago\n'
                                              f'ISO CODE : TT/TTO')
            enter(message)


##############################################################################################################
# Tunisia            #
##############################################################################################################

        elif message.text == 'Tunisia' or message.text == 'tunisia':
            bot.send_message(message.chat.id, f'Country CODE : +216\n'
                                              f'ISO CODE : TN/TUN')
            enter(message)



        elif message.text == '216' or message.text == '+216':
            bot.send_message(message.chat.id, f'Country  : Tunisia\n'
                                              f'ISO CODE : TN/TUN')
            enter(message)

##############################################################################################################
# Turkey            #
##############################################################################################################

        elif message.text == 'Turkey' or message.text == 'turkey':
            bot.send_message(message.chat.id, f'Country CODE : +90\n'
                                              f'ISO CODE : TR/TUR')
            enter(message)



        elif message.text == '90' or message.text == '+90':
            bot.send_message(message.chat.id, f'Country  : Turkey\n'
                                              f'ISO CODE : TR/TUR')
            enter(message)


##############################################################################################################
# Turkmenistan            #
##############################################################################################################

        elif message.text == 'Turkmenistan' or message.text == 'turkmenistan':
            bot.send_message(message.chat.id, f'Country CODE : +993\n'
                                              f'ISO CODE : TM/TKM')
            enter(message)



        elif message.text == '993' or message.text == '+993':
            bot.send_message(message.chat.id, f'Country  : Turkmenistan\n'
                                              f'ISO CODE : TM/TKM')
            enter(message)

##############################################################################################################
# Turks and Caicos Islands            #
##############################################################################################################

        elif message.text == 'Turks and Caicos Islands' or message.text == 'Turks and caicos islands' or message.text == 'turks and caicos islands':
            bot.send_message(message.chat.id, f'Country CODE : +1-649\n'
                                              f'ISO CODE : TC/TRC')
            enter(message)



        elif message.text == '1-649' or message.text == '+1-649':
            bot.send_message(message.chat.id, f'Country  : Turks and Caicos Islands\n'
                                              f'ISO CODE : TC/TRC')
            enter(message)



##############################################################################################################
# Tuvalu            #
##############################################################################################################

        elif message.text == 'Tuvalu' or message.text == 'tuvalu':
            bot.send_message(message.chat.id, f'Country CODE : +688\n'
                                              f'ISO CODE : TV/TUV')
            enter(message)



        elif message.text == '688' or message.text == '+688':
            bot.send_message(message.chat.id, f'Country  : Tuvalu\n'
                                              f'ISO CODE : TV/TUV')
            enter(message)

##############################################################################################################
# U.S Virgin Islands           #
##############################################################################################################

        elif message.text == 'U.S Virgin Islands' or message.text == 'U.S virgin islands' or message.text == 'u.s virgin Islands':
            bot.send_message(message.chat.id, f'Country CODE : +1-340\n'
                                              f'ISO CODE : VI/VIR')
            enter(message)



        elif message.text == '1-340' or message.text == '+1-340':
            bot.send_message(message.chat.id, f'Country  : U.S Virgin Islands\n'
                                              f'ISO CODE : VI/VIR')
            enter(message)


##############################################################################################################
# Uganda           #
##############################################################################################################

        elif message.text == 'Uganda' or message.text == 'uganda':
            bot.send_message(message.chat.id, f'Country CODE : +256\n'
                                              f'ISO CODE : VI/VIR')
            enter(message)



        elif message.text == '256' or message.text == '+256':
            bot.send_message(message.chat.id, f'Country  : Uganda\n'
                                              f'ISO CODE : VI/VIR')
            enter(message)

##############################################################################################################
# Ukraine           #
##############################################################################################################

        elif message.text == 'Ukraine' or message.text == 'ukraine':
            bot.send_message(message.chat.id, f'Country CODE : +380\n'
                                              f'ISO CODE : UA/UK')
            enter(message)



        elif message.text == '380' or message.text == '+380':
            bot.send_message(message.chat.id, f'Country  : Ukraine\n'
                                              f'ISO CODE : UA/UK')
            enter(message)

##############################################################################################################
# United Arab Emirates           #
##############################################################################################################

        elif message.text == 'United Arab Emirates' or message.text == 'United arab emirates' or message.text == 'united arab emirates' or message.text == 'UAE':
            bot.send_message(message.chat.id, f'Country CODE : +380\n'
                                              f'ISO CODE : UA/UK')
            enter(message)



        elif message.text == '380' or message.text == '+380':
            bot.send_message(message.chat.id, f'Country  : Uganda\n'
                                              f'ISO CODE : UA/UK')
            enter(message)

##############################################################################################################
# United Kindgom           #
##############################################################################################################

        elif message.text == 'United Kingdom' or message.text == 'United kingdom' or message.text == 'United kingdom' or message.text == 'UK' or message.text == 'Uk' or message.text == 'uk':
            bot.send_message(message.chat.id, f'Country CODE : +44\n'
                                              f'ISO CODE : GB/GBR')
            enter(message)



        elif message.text == '44' or message.text == '+44':
            bot.send_message(message.chat.id, f'Country  : United Kindgom\n'
                                              f'ISO CODE : GB/GBR')
            enter(message)


##############################################################################################################
# United States         #
##############################################################################################################

        elif message.text == 'United States' or message.text == 'United states' or message.text == 'united States' or message.text == 'usa' or message.text == 'USA' or message.text == 'United States of America' or message.text == 'United states of america' or message.text == 'united states of america':
            bot.send_message(message.chat.id, f'Country CODE : +1\n'
                                              f'ISO CODE : US/USA')
            enter(message)



##############################################################################################################
# Uruguay          #
##############################################################################################################

        elif message.text == 'Uruguay' or message.text == 'uruguay':
            bot.send_message(message.chat.id, f'Country CODE : +598\n'
                                              f'ISO CODE : UY/URY')
            enter(message)



        elif message.text == '598' or message.text == '+598':
            bot.send_message(message.chat.id, f'Country  : Uruguay\n'
                                              f'ISO CODE : UY/URY')
            enter(message)


##############################################################################################################
# Uzbekistan          #
##############################################################################################################

        elif message.text == 'Uzbekistan' or message.text == 'uzbekistan':
            bot.send_message(message.chat.id, f'Country CODE : +998\n'
                                              f'ISO CODE : UZ/UZB')
            enter(message)



        elif message.text == '998' or message.text == '+998':
            bot.send_message(message.chat.id, f'Country  : Uzbekistan\n'
                                              f'ISO CODE : UZ/UZB')
            enter(message)

##############################################################################################################
# Vanautu          #
##############################################################################################################

        elif message.text == 'Vanautu' or message.text == 'vanautu':
            bot.send_message(message.chat.id, f'Country CODE : +678\n'
                                              f'ISO CODE : VU/VUT')
            enter(message)



        elif message.text == '678' or message.text == '+678':
            bot.send_message(message.chat.id, f'Country  : Vanautu\n'
                                              f'ISO CODE : VU/VUT')
            enter(message)


##############################################################################################################
# Vatican         #
##############################################################################################################

        elif message.text == 'Vatican' or message.text == 'vatican':
            bot.send_message(message.chat.id, f'Country CODE : +379\n'
                                              f'ISO CODE : VA/VAT')
            enter(message)



        elif message.text == '379' or message.text == '+379':
            bot.send_message(message.chat.id, f'Country  : Vatican\n'
                                              f'ISO CODE : VA/VAT')
            enter(message)

##############################################################################################################
# Venezuela         #
##############################################################################################################

        elif message.text == 'Venezuela' or message.text == 'venezuela':
            bot.send_message(message.chat.id, f'Country CODE : +58\n'
                                              f'ISO CODE : VE/VEN')
            enter(message)



        elif message.text == '58' or message.text == '+58':
            bot.send_message(message.chat.id, f'Country  : Venezuela\n'
                                              f'ISO CODE : VE/VEN')
            enter(message)

##############################################################################################################
# Vietnam         #
##############################################################################################################

        elif message.text == 'Vietnam' or message.text == 'vietnam':
            bot.send_message(message.chat.id, f'Country CODE : +84\n'
                                              f'ISO CODE : VN/VNM')
            enter(message)



        elif message.text == '84' or message.text == '+84':
            bot.send_message(message.chat.id, f'Country  : Vietnam\n'
                                              f'ISO CODE : VN/VNM')
            enter(message)



##############################################################################################################
# Wallis and Futuna         #
##############################################################################################################

        elif message.text == 'Wallis and Futuna' or message.text == 'Wallis and futuna' or message.text == 'wallis and futuna':
            bot.send_message(message.chat.id, f'Country CODE : +681\n'
                                              f'ISO CODE : WF/WLF')
            enter(message)



        elif message.text == '681' or message.text == '+681':
            bot.send_message(message.chat.id, f'Country  : Wallis and Futuna\n'
                                              f'ISO CODE : WF/WLF')
            enter(message)

##############################################################################################################
# Western Sahara        #
##############################################################################################################

        elif message.text == 'Western Sahara' or message.text == 'Western sahara' or message.text == 'western sahara':
            bot.send_message(message.chat.id, f'Country CODE : +212\n'
                                              f'ISO CODE : EH/ESH')
            enter(message)


##############################################################################################################
# Yemen        #
##############################################################################################################

        elif message.text == 'Yemen' or message.text == 'yemen':
            bot.send_message(message.chat.id, f'Country CODE : +967\n'
                                              f'ISO CODE : YE/YEM')
            enter(message)



        elif message.text == '967' or message.text == '+967':
            bot.send_message(message.chat.id, f'Country  : Yemen\n'
                                              f'ISO CODE : YE/YEM')
            enter(message)


##############################################################################################################
# Zambia        #
##############################################################################################################

        elif message.text == 'Zambia' or message.text == 'zambia':
            bot.send_message(message.chat.id, f'Country CODE : +260\n'
                                              f'ISO CODE : ZM/ZMB')
            enter(message)



        elif message.text == '260' or message.text == '+260':
            bot.send_message(message.chat.id, f'Country  : Zambia\n'
                                              f'ISO CODE : YE/YEM')
            enter(message)

##############################################################################################################
# Zimbabwe        #
##############################################################################################################

        elif message.text == 'Zimbabwe' or message.text == 'zimbabwe':
            bot.send_message(message.chat.id, f'Country CODE : +263\n'
                                              f'ISO CODE : ZW/ZWE')
            enter(message)



        elif message.text == '263' or message.text == '+263':
            bot.send_message(message.chat.id, f'Country  : Zimbabwe\n'
                                              f'ISO CODE : ZW/ZWE')
            enter(message)


        elif message.text == 'Back':
             mainmenu(message)


        elif message.text == 'Exchange rate':
             curmenu(message)









#Correctmessage
######################################
        else:
            correct(message)
#########################################


    except:
        correct(message)


























bot.polling()
