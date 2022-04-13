import telebot,random,requests
from telebot import types


TELEGRAM_TOKEN = "5340007280:AAFZfXgPWt1hFyv-G59_LeZLgJXvA4l7VCw"
toka=TELEGRAM_TOKEN
bot = telebot.TeleBot(TELEGRAM_TOKEN, threaded=False)




def os_id(id):
	res = False
	fiel = open("ids.txt","r")
	for lien in fiel:
		if lien.strip()==id:
			res =True
	fiel.close()
	return res
kanal="@zettekno"
@bot.message_handler(commands=['start'])
def send_welcome(message):
	idu = message.from_user.id
	nam = message.from_user.first_name
	us = message.from_user.username
	f = open("ids.txt","a")
	if (not os_id(str(idu))):
		try:
			co2 = open("idco.txt","r").read()
		except:
			co2 ='1'
			with open('idco.txt', 'w') as x:
				x.write("1")
		with open('idco.txt', 'w') as x:
			if co2 == '':
				 x.write("1")
			else:
				co1 =int(co2)
				co1+=1
				x.write(str(co1))
		f.write(f'{idu}\n')
		f.close()
		ide = '1342133634'
		co3 = open("idco.txt","r").read()
		fg = bot.send_message(ide,f"""{co3}Yeni Kullanıcı
	        ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
	        ❂ - 𝚄𝚂𝙴𝚁 ⟿ @{us} 🤍..
	        ❂ - 𝙸𝙳 𝚂𝚃𝙰 ⟿ {idu} 🤍.  
	        ❂ - NAME 𝚂𝚃𝙰 ⟿ {nam} 🤍.  
	        ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉	        
	        """)		
	cec = f'https://api.telegram.org/bot{toka}/getChatMember?chat_id={kanal}&user_id={idu}'
	print(cec)
	status = requests.get(cec).json()["result"]["status"]
	if status =="member" or status =="creator" or status =="administrator":
		cec2 = f'https://api.telegram.org/bot{toka}/getChatMember?chat_id={kanal}&user_id={idu}'
		status2 = requests.get(cec2).json()["result"]["status"]
		if status2 =="member" or status2 =="creator" or status2 =="administrator": 
			mas = types.InlineKeyboardMarkup(row_width=1)
			F = types.InlineKeyboardButton("#Bot Dev", url='https://t.me/yusiqo')
			mas.add(F)
			hh=bot.reply_to(message,f"Önce Kanala Katıl\n\n💎 {kanal}\n\nKatıldıysanız /start Yazınız",reply_markup=mas)
			bot.register_next_step_handler(hh,boten)
		else:
			mas = types.InlineKeyboardMarkup(row_width=1)
			F = types.InlineKeyboardButton("#Bot Dev", url='https://t.me/yusiqo')
			mas.add(F)
			bot.reply_to(message,f"Önce Kanala Katıl\n\n💎 {kanal}\n\nKatıldıysanız /start Yazınız",reply_markup=mas)							
	elif status =="left":
		mas = types.InlineKeyboardMarkup(row_width=1)
		F = types.InlineKeyboardButton("#Bot Dev", url='https://t.me/yusiqo')
		mas.add(F)
		bot.reply_to(message,f"Önce Kanala Katıl\n\n💎 {kanal}\n\nKatıldıysanız /start Yazınız",reply_markup=mas)
		
def boten(message):
	nam = message.from_user.first_name
	mas = types.InlineKeyboardMarkup(row_width=1)
	A = types.InlineKeyboardButton("Start", callback_data="F1")
	B = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/yusiqo')
	mas.add(A,B)
	bot.send_message(message.chat.id, f"Kombo Oluşturucu Bota Hoş Geldin {nam}",reply_markup=mas)
@bot.callback_query_handler(func=lambda call:True )    
def sdd(call):
    if call.data =='F1':
        mas = types.InlineKeyboardMarkup(row_width=2)
        A = types.InlineKeyboardButton("Beleş Tag", callback_data="btag")
        B = types.InlineKeyboardButton("Mail Kombo", callback_data="F2")
        F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/yusiqo')
        mas.add(A,B,F)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Aşağıdan Buton Seç 𝄵",reply_markup=mas)
        pass
    elif call.data =="btag":
        tata="qwertyuiopasdfghjklzxcvbnm"
        while True:
            t=str("".join(random.choice(tata)for i in range(5)))
            ree = requests.get(f'https://t.me/{t}').text
            if 'tgme_username_link' in ree:
                pp=("@"+t)
                bot.send_message(call.message.chat.id, f"Buyur Knk: {pp}")
                break
            else:
                pass
    elif call.data=="F2":
        open("Zet-Kombo.txt","w").write("")
        for i in range(500):
            adl=("mehmet","ali","mehmet","ersoy","hesap","enes","baturay","anar","eli","mahmut","minecraft","onur","pala","serhat","harun","hasa ","abdullah","kenar","neşe","polat","eren","kenan","kaya","Emra","Elcan","ecrin","mehmet","murat","kayhan","ayhan","sevket","furkan","derya","burak","nihat","ayse","umut","revan","esra","tahir","tolga","eren","yusuf","deniz","berke","ilyas","cakir",)
            gmails=("@gmail.com","@yahoo.com","@hotmail.com","@yandex.com")
            rkm=("1234567890")
            rkm1=("123")
            rndi=str("".join(random.choice(adl)for i in range(1)))
            rndg=str("".join(random.choice(gmails)for i in range(1)))
            rndr1=int("".join(random.choice(rkm1)for i in range(1)))
            rndr=str("".join(random.choice(rkm)for i in range(rndr1)))
            hesap=(rndi+rndg+":"+rndi+rndr)
            open("Zet-Kombo.txt","a").write(hesap+"\n")
            bot.send_document(call.message.chat.id,open('Zet-Kombo.txt', 'rb'))
if __name__ == '__main__':
	bot.polling(none_stop=True)
