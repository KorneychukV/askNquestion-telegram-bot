import telebot
import sys
from telebot import types

if __name__ == "__main__":
    token = sys.argv[1]
    bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_words = ('Приятно познакомиться, ', message.from_user.first_name, '. Я бот ask&question.')
    welcome_message = ''.join(str(w) for w in welcome_words)
    bot.reply_to(message, welcome_message)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() == 'check':
        keyboard = types.InlineKeyboardMarkup()
        like_button= types.InlineKeyboardButton(text="Like", callback_data='like')
        keyboard.add(like_button)
        dislike_button =types.InlineKeyboardButton (text="Dislike", callback_data='dislike')
        keyboard.add(dislike_button)
        bot.send_message(message.from_user.id, 'Are you like cats?', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == 'like':
        answer = 'You like it!'
    elif call.data == "dislike":
        answer = "You don't like it!"
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling(none_stop=True)