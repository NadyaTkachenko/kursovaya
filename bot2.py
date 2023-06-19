import telebot
from config2 import token
from telebot import types

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text='да')
    keyboard2 = types.KeyboardButton(text='нет')
    markup.add(keyboard, keyboard2)
    bot.send_message(chat_id, f'Привет!,{first_name}, узнаем насколько ты знаешь страны?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text.lower() == 'да':
            bot.send_message(chat_id, 'Отлично! Начинаем!')
            bot.send_message(chat_id, 'Какая это страна?')
            inline_markup = telebot.types.InlineKeyboardMarkup()
            inline_keyboard = types.InlineKeyboardButton('Египет', callback_data='1')
            inline_keyboard2 = types.InlineKeyboardButton('Мексика', callback_data='2')
            inline_markup.row(inline_keyboard, inline_keyboard2)
            bot.send_photo(message.chat.id,
                           photo="https://funart.pro/uploads/posts/2019-11/1573817984_piramidy-v-gize-egipet-50.jpg",
                           reply_markup=inline_markup)

        elif message.text.lower() == 'нет':
            bot.send_message(chat_id, 'Жаль,пока!')


@bot.message_handler(content_types=["text"])
def text_2(message):
    chat_id_2 = message.chat.id
    if message.chat.type == 'private':
        if message.text.lower() == 'да':
            inline_markup = telebot.types.InlineKeyboardMarkup()
            inline_keyboard_3 = types.InlineKeyboardButton('Испания', callback_data='3')
            inline_keyboard_4 = types.InlineKeyboardButton('Франция', callback_data='4')
            inline_markup.row(inline_keyboard_3, inline_keyboard_4)
            bot.send_photo(message.chat.id,
                    photo="http://voltagerider.com/wp-content/uploads/2020/05/electric_scooter_types.jpg",
                    reply_markup=inline_markup)

        elif message.text.lower() == 'нет':
            bot.send_message(chat_id_2, 'Жаль,пока!')


@bot.callback_query_handler(func=lambda callback: callback.data)
def chek_callback_data(callback):
    if callback.data in ('1'):
        bot.send_message(callback.message.chat.id, 'Все верно!')
        bot.send_message(callback.message.chat.id,
                         'Интересный факт: Египетские пирамиды — каменные сооружения, используемые древними царями '
                         'как усыпальницы, храмы и казнохранилища. '
                         'Сохранилось 118 пирамид, которые расположены у берегов реки Нил, на севере Египта.')

    elif callback.data == '2':
        bot.send_message(callback.message.chat.id, 'Не верно( Попробуй еще раз!')


    if callback.data in ('4'):
        bot.send_message(callback.message.chat.id, 'Умничка!')
        bot.send_message(callback.message.chat.id,
                     'Интересный факт: Эта страна - лидер по посещаемости.'
                     'Каждый год количество туристов превышает население страны')
    elif callback.data == '3':
        bot.send_message(callback.message.chat.id, 'Не верно( Попробуй еще раз!')
    if callback.data in ('5'):
        bot.send_message(callback.message.chat.id, 'Молодец!')
        bot.send_message(callback.message.chat.id,
                     'На территории Италии расположены два '
                     'мини-государства - Сан-Марино и Ватикан.')
    elif callback.data == '6':
        bot.send_message(callback.message.chat.id, 'Не верно( Попробуй еще раз!')

    msg = bot.send_message(callback.message.chat.id, 'Еще?')
    bot.register_next_step_handler(msg, text_2)
    
    bot.register_next_step_handler( msg,text_3)


@bot.message_handler(content_types=["text"])
def text_3(message):
    chat_id_3 = message.chat.id
    if message.chat.type == 'private':
        inline_markup = telebot.types.InlineKeyboardMarkup()
        inline_keyboard5 = types.InlineKeyboardButton('Италия', callback_data='5')
        inline_keyboard6 = types.InlineKeyboardButton('Черногория', callback_data='6')
        inline_markup.row(inline_keyboard5, inline_keyboard6)
        bot.send_photo(message.chat.id,
                       photo="http://topmesta.ru/wp-content/uploads/dostoprimechatelnosti-italii-1.jpg",
                       reply_markup=inline_markup)
bot.polling(none_stop=True, interval=0)