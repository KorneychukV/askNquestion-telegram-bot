import telebot

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, ('Приятно познакомиться, ', {message.from_user.first_name}, '. Я бот ask&question. )
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)

if __name__ == "__main__":
    token = int(sys.argv[1])