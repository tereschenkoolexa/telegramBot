import telebot
import sys

bot = telebot.TeleBot('5714768365:AAEetAVNSL3mUkkyBgWrKCq1y-xkUVF5WG0')

@bot.message_handler(commands=['hello'])
def start(message):
    mess = f'Привіт, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    try:
        if message.via_bot:
            if message.via_bot.is_bot:
                bot.delete_message(message.chat.id, message.id)
    except:
        print("Oops! occurred.")



bot.polling(none_stop=True)
