import random

import telebot
import cld2
from langdetect import detect

import sys
from datetime import datetime, timedelta

priorMessageSticker = ''
priorMessageStickerTime = 0
priorMessageStickerUser = ''

priorMessageDocument = ''

priorMessageAnimation = ''
priorMessageAnimationUser = ''
priorMessageAnimationTime = 0

priorMessagePhoto = 0

priorMessageTextTime = 0
priorMessageTextUser = ''

def fillingSticker(str, str2, str3):
    global priorMessageSticker
    priorMessageSticker = str
    global priorMessageStickerTime
    priorMessageStickerTime = str2
    global priorMessageStickerUser
    priorMessageStickerUser = str3

def fillingDocument(str):
    global priorMessageDocument
    priorMessageDocument = str

def fillingAnimation(str, strU, strT):
    global priorMessageAnimation
    priorMessageAnimation = str
    global priorMessageAnimationUser
    priorMessageAnimationUser = strU
    global priorMessageAnimationTime
    priorMessageAnimationTime = strT

def fillingPhoto(str):
    global priorMessagePhoto
    priorMessagePhoto = str

def fillingText(str, str2):
    global priorMessageTextTime
    priorMessageTextTime = str
    global priorMessageTextUser
    priorMessageTextUser = str2

bot = telebot.TeleBot('5714768365:AAEetAVNSL3mUkkyBgWrKCq1y-xkUVF5WG0')

bullyingSentenceY = ['Як там собачки?','Коли аніме на аву поставиш?','Колінка ще болять?','Кочермякай',
                    'Going to your mum', 'Твоя мама сьогодні у Олега', 'Ти русня', 'БТС це музика для 12 річних',
                    'Івана 4: 10-14: \nІсус відповів і сказав їй: Якщо ти знаєш дар Божий і хто тобі каже, дай мені пити; ти б попросив у нього, і він дав би тобі живу воду. 11 Жінка каже до нього: Господи, ти не маєш із чим малювати, а криниця глибока. Звідки ти живу воду? 12 Чи ти більший за нашого батька Якова, що дав нам криницю, і пив її сам, і діти його, і худоба його? 13 Ісус відповів і сказав їй: Хто питиме цієї води, той знову спрагне; 14 а хто питиме води, яку Я дам йому, ніколи не спрагне; а вода, яку Я дам йому, буде в ньому криницею води, що виливається у життя вічне.',
                    'Нюхай бебру', 'Ти генератор крінжі', 'Іди далі собачок гвалтуй','Засунь в сраку свій Клєш Роял',
                    '🫵 Чмоня','Ну тобі реально 5 рочків', 'Зоофілів не питали']
bullyingSentence = ['Мама жива?','Офнись попущ','Йди нахуй, нуліна','Кочермякай', 'Ти Агент Кремля',
                    'Ти знаєш, що ти просто нікчемність?', 'За тебе навіть Владік краще',
                    'Ніхуя ти бздюх', 'Бля, тіп висрись назад в пізду своєї мамаши',
                    'Єбать ти Піпівозавр', 'Гімно дауна лівни нахуй', 'Хуй залупа підарас',
                    'Твоя мать не шлюха? А звідки у неї такий випердиш?', 'Нігер',
                    'Ти хуйлан', 'Як поживаєш малопіькович?', 'Анус переляканий']

antiFlood = []

checklist = {"ы", "ё", "э", "ъ", "россия", "мать", "да", "нет", 'Ѣ', 'из-за',
             'если','кста','когда','только','папа','какая','шь', 'почему'}

agentKreml = ['valkyrgoddess', 'kycyk_myavcyk', 'batislavskiy']



@bot.message_handler(commands=['hello'])
def start(message):
    mess = f'Привіт, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')
@bot.message_handler(commands=['bullyingY'])
def start(message):
    mess = f'@kycyk_myavcyk, {bullyingSentenceY[random.randint(0, 15)]}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['bullying'])
def start(message):
    try:
        if message.from_user.username == "kycyk_myavcyk":
            bot.send_message(message.chat.id, 'Та йди ти нахуй, Ярик їбаний', parse_mode='html')
        else:
            command = message.text.split(maxsplit=1)[1]
            mess = f'{command}, {bullyingSentence[random.randint(0, 15)]}'
            bot.send_message(message.chat.id, mess, parse_mode='html')
    except:
        bot.send_message(message.chat.id, 'Хуйлуша тегни когось', parse_mode='html')

@bot.message_handler(commands=['based'])
def start(message):
    bot.send_animation(message.chat.id, animation=open('based.mp4', 'rb'))
@bot.message_handler(commands=['help'])
def start(message):
    mess = f'/hello - привітання' \
           f'\n/help - список команд'\
           f'\n/bullyingY - булінг Ярослава'\
           f'\n/bullying - булінг'\
           f'\n/based - база'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=["sticker"])
def start(message):
    ruslanDyshnila = 29232
    ruslanDyshnila2 = 20072
    messageTime = message.date - priorMessageStickerTime
    if message.sticker.file_size == ruslanDyshnila or message.sticker.file_size == ruslanDyshnila2:
        bot.delete_message(message.chat.id, message.id)
    elif priorMessageSticker == message.sticker.file_unique_id and messageTime < 2 or messageTime < 2 and priorMessageStickerUser == message.from_user.username:
        bot.delete_message(message.chat.id, message.id)
        fillingSticker(message.sticker.file_unique_id, message.date, message.from_user.username)
    else:
        fillingSticker(message.sticker.file_unique_id, message.date, message.from_user.username)


@bot.message_handler(commands=['help_me', 'save_me'])
def start(message):
    mess = f'Кочермякай, @{message.from_user.username}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):

    try:
        if message.via_bot:
            if message.via_bot.is_bot:
                bot.delete_message(message.chat.id, message.id)
        elif priorMessageTextUser == message.from_user.username:
            messageTime = message.date - priorMessageTextTime
            if messageTime < 2 and messageTime > 0:
                bot.delete_message(message.chat.id, message.id)
            fillingText(message.date, message.from_user.username)
        else:
            fillingText(message.date, message.from_user.username)

        if "Ярос" in message.text:
            if random.randint(0, 1) == 0:
                bot.send_message(message.chat.id, 'ТА ЙДИ ТИ НАХУЙ ЗІ СВОЇМ ЯРОСЛАВОМ', parse_mode='html')

        if message.forward_from:
            if random.randint(0, 6) == 5:
                bot.send_message(message.chat.id, F'Дякую, @{message.from_user.username}, що ділишся з нами цим', parse_mode='html')
        else:
            lang = detect(message.text)
            print(str(lang))
            if lang == 'uk':
                if random.randint(0, 600) == 5:
                    bot.send_message(message.chat.id, 'Ви любите спілі кавунчики?',parse_mode='html')
            else:
                Bool = any(map(message.text.lower().__contains__, map(str.lower, checklist)))
                if Bool:
                    bot.delete_message(message.chat.id, message.id)
                    if random.randint(0, 6) == 5:
                        bot.send_message(message.chat.id, 'Бібок, тут заборонено писати на російські, лише українською', parse_mode='html')

        if message.from_user.username == agentKreml[random.randint(0, 2)]:
            print(random.randint(0, 2))
            if random.randint(0, 30) == 5:
                bot.send_message(message.chat.id, f"@{message.from_user.username} ти <b>ця людина являється Агентом Кремля, читайте її з обережністю</b>", parse_mode='html')
    except:
        print("Oops! occurred in text.")

@bot.message_handler(content_types=['document'])
def start(message):
    try:
        if message.document.file_size == 334693:
            bot.delete_message(message.chat.id, message.id)
        elif priorMessageDocument == message.document.file_size:
            bot.delete_message(message.chat.id, message.id)
        else:
            fillingDocument(message.document.file_size)
    except:
        print("Oops! occurred in document.")
@bot.message_handler(content_types=['photo'])
def start(message):
    try:
        if message.photo[2].file_size == 46937:
            bot.delete_message(message.chat.id, message.id)
        if message.forward_from_chat.type == 'channel':
            if random.randint(0, 6) == 5:
                bot.send_message(message.chat.id, 'Тіп, дуже цікавий форвад, з картинкою навіть', parse_mode='html')
        else:
            if priorMessagePhoto == message.photo[2].file_size:
                bot.delete_message(message.chat.id, message.id)
            else:
                fillingPhoto(message.photo[2].file_size)
    except:
        print("Oops! occurred in photo.")

@bot.message_handler(content_types=['animation'])
def start(message):
    try:
        if random.randint(0, 10) == 5:
            bot.send_message(message.chat.id, 'Я тоже вмію гіфку кидати', parse_mode='html')
            bot.send_animation(message.chat.id, animation=open('watermalonbabah.gif', 'rb'))
        messageTime = message.date - priorMessageAnimationTime
        if priorMessageAnimation == message.document.file_unique_id and messageTime < 2 or messageTime < 2 and priorMessageAnimationUser == message.from_user.username:
            bot.delete_message(message.chat.id, message.id)
            fillingAnimation(message.document.file_unique_id, message.from_user.username, message.date)
        else:
            fillingAnimation(message.document.file_unique_id, message.from_user.username, message.date)
    except:
        print("Oops! occurred in animation.")

bot.polling(none_stop=True)
