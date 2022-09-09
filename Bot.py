import telebot
import sys
from datetime import datetime, timedelta

bot = telebot.TeleBot('5714768365:AAEetAVNSL3mUkkyBgWrKCq1y-xkUVF5WG0')

@bot.message_handler(commands=['hello'])
def start(message):
    mess = f'Привіт, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=["sticker"])
def start(message):
    if message.sticker.file_unique_id == 'AgADwhgAArecOEg':
        bot.delete_message(message.chat.id, message.id)

@bot.message_handler(commands=['help'])
def start(message):
    mess = f'/hello - привітання' \
           f'\n/help - список команд'
    bot.send_message(message.chat.id, mess, parse_mode='html')
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
    #        if message.from_user.username == "batislavskiy":
#            bot.send_message(message.chat.id, f"@{message.from_user.username} ти <b>Агент Кремля</b>", parse_mode='html')
    except:
        print("Oops! occurred.")



bot.polling(none_stop=True)
