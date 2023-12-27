from telebot import telebot, types
import os

TOKEN = os.environ.get('TG_TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "*Sawadika 🙏🏻🙏🏻🙏🏻*\n" \
           "_How are you doing?_\n\n" \
           "This is Telegram bot written in Python🐍!\n" \
           "If any problems contact 👨🏻‍💻[admin](tg://user?id=360841329)\n\n" \
           f"🏖️🏞Please see all sightseeing/attraction options from /allsights.\n\n" \
           f"🌄View points /views.\n" \
           f"🏯Temples /temples.\n" \
           f"👙Activities /activities.\n" \
           f"👫Touristic places /touristic.\n" \
           f"🛍️Shopping /shopping.\n"
    bot.send_message(message.from_user.id, text=text, parse_mode="markdown")

# commands
# allsights - all sightseeing/attraction options
# views - view points
# temples - temples around
# activities - sports, beaches, and more
# touristic - list of touristic places
# shopping - shopping malls

# @bot.message_handler(commands=['menu'])
# def send_menu(message):
#     text = "*Please select sightseeing option from Menu:*"
#     markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
#     itembtn1 = types.KeyboardButton(text='Top 1(0')
#     itembtn2 = types.KeyboardButton('By Location')
#     itembtn3 = types.KeyboardButton('By Activity')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.send_message(message.from_user.id, text=text, parse_mode="markdown", reply_markup=markup)


@bot.message_handler(commands=['allsights'])
def sights_all(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text='The Sanctuary Of Truth',
                                          url='https://maps.app.goo.gl/jrbzuZnBxuHbWsbCA',
                                          callback_data='sanctuary_of_truth'),
               types.InlineKeyboardButton(text='Pattaya Tower',
                                          url='https://maps.app.goo.gl/UKk5NKxRUhtbCHb4A'),
               types.InlineKeyboardButton(text='Big Buddha Temple',
                                          url='https://maps.app.goo.gl/Zb4g66XPDz8LPDe38'),
               types.InlineKeyboardButton(text='Pattaya Floating Market',
                                          url='https://maps.app.goo.gl/d5hWtqVmJcEfE4zN9'),
               types.InlineKeyboardButton(text='Pattaya City Sign',
                                          url='https://maps.app.goo.gl/T6FGs2UBuqqPApWu6'),
               types.InlineKeyboardButton(text='Phra Tamnak Mountain Viewpoint',
                                          url='https://maps.app.goo.gl/Kfk6gUwsGNUhfmx77'),
               types.InlineKeyboardButton(text='Pattaya Walking Street',
                                          url='https://maps.app.goo.gl/ccF8PaUjUuDJAXjz8'),
               types.InlineKeyboardButton(text='The Lunar Beach House',
                                          url='https://maps.app.goo.gl/UQNcRmqz8apRyLNYA'),
               types.InlineKeyboardButton(text='Jomtien Heads Viewpoint',
                                          url='https://maps.app.goo.gl/L4jyupzAoPTTQRWBA'),
               types.InlineKeyboardButton(text='Underwater World Pattaya',
                                          url='https://maps.app.goo.gl/Vc2G8FjyLPFKTzkB9'),
               types.InlineKeyboardButton(text='Windsurfing Club',
                                          url='https://maps.app.goo.gl/Xn268yxqeBNyG2hb8'),
               types.InlineKeyboardButton(text='Wat Huay Yai',
                                          url='https://maps.app.goo.gl/p7s37kVn7RK9CeLF6'),
               types.InlineKeyboardButton(text='Legend Siam Pattaya',
                                          url='https://maps.app.goo.gl/7cfqcRVaf9cEBDb39'),
               types.InlineKeyboardButton(text='Nongnooch Tropical Garden Pattaya',
                                          url='https://maps.app.goo.gl/T3k52mzMuHPX4BK87'),
               types.InlineKeyboardButton(text='Ramayana Water Park',
                                          url='https://maps.app.goo.gl/FspyF7R8qWSk6hL88'),
               types.InlineKeyboardButton(text='Khao Chi Chan Buddha',
                                          url='https://maps.app.goo.gl/Cw33fihRJFdNJydW6'),
               types.InlineKeyboardButton(text='Viharn Sien',
                                          url='https://maps.app.goo.gl/NfUCQiQqkN8NrURe9'),
               types.InlineKeyboardButton(text='Wat Yan Nasangwararam Woramahawihan',
                                          url='https://maps.app.goo.gl/bGyxLnxxmBp2RGkf8'),
               types.InlineKeyboardButton(text='Buddhist temple',
                                          url='https://maps.app.goo.gl/9rZSHmgvEzfMbooXA'),
               types.InlineKeyboardButton(text='Wat Yanasangwararam',
                                          url='https://maps.app.goo.gl/o3wYVTotGY7nxBmr8'),
               types.InlineKeyboardButton(text='Columbia Pictures Aquaverse',
                                          url='https://maps.app.goo.gl/hgmEQ1SKKP2buA1QA'),
               types.InlineKeyboardButton(text='Temple',
                                          url='https://maps.app.goo.gl/9R8rSZVEFPwNB4ZQ9'),
               types.InlineKeyboardButton(text='Ubosoth Wat Song Metta Wanaram',
                                          url='https://maps.app.goo.gl/UJjTvV3rWU2pDUXCA'),
               types.InlineKeyboardButton(text='Wat Khao Khanthamat',
                                          url='https://maps.app.goo.gl/doR1GZAeqfdJzX7VA'),
               types.InlineKeyboardButton(text='Wat Sattahip (Wat Luang Pho Yi)',
                                          url='https://maps.app.goo.gl/YbgAZuonz875B9KS7'),
               types.InlineKeyboardButton(text='Sea View',
                                          url='https://maps.app.goo.gl/At4MgHykgMnzk2cq6'),
               types.InlineKeyboardButton(text='Ko Lan Island',
                                          url='https://maps.app.goo.gl/C1bABSaEkCoubjFK9'),
               types.InlineKeyboardButton(text='Khram Yai Island',
                                          url='https://maps.app.goo.gl/Mb6QY6WtTvgs7Zv98'),
               types.InlineKeyboardButton(text='Mini Siam',
                                          url='https://maps.app.goo.gl/LDmx6nrN8Dgxcup9A'),
               types.InlineKeyboardButton(text='Terminal 21 Pattaya',
                                          url='https://maps.app.goo.gl/YrRNCjspYsLMcneMA'),
               types.InlineKeyboardButton(text='Central Pattaya',
                                          url='https://maps.app.goo.gl/bbo4GAez8KwTvZy16'),
               ]
    text = "These are top sights to see in Pattaya:"
    markup.add(*buttons)
    bot.send_message(chat_id=message.from_user.id,
                     text=text,
                     reply_markup=markup)


@bot.message_handler(commands=['views'])
def sights_views(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text='The Sanctuary Of Truth',
                                          url='https://maps.app.goo.gl/jrbzuZnBxuHbWsbCA'),
               types.InlineKeyboardButton(text='Big Buddha Temple',
                                          url='https://maps.app.goo.gl/Zb4g66XPDz8LPDe38'),
               types.InlineKeyboardButton(text='Pattaya City Sign',
                                          url='https://maps.app.goo.gl/T6FGs2UBuqqPApWu6'),
               types.InlineKeyboardButton(text='Phra Tamnak Mountain Viewpoint',
                                          url='https://maps.app.goo.gl/Kfk6gUwsGNUhfmx77'),
               types.InlineKeyboardButton(text='The Lunar Beach House',
                                          url='https://maps.app.goo.gl/UQNcRmqz8apRyLNYA'),
               types.InlineKeyboardButton(text='Jomtien Heads Viewpoint',
                                          url='https://maps.app.goo.gl/L4jyupzAoPTTQRWBA'),
               types.InlineKeyboardButton(text='Windsurfing Club',
                                          url='https://maps.app.goo.gl/Xn268yxqeBNyG2hb8'),
               types.InlineKeyboardButton(text='Sea View',
                                          url='https://maps.app.goo.gl/At4MgHykgMnzk2cq6'),
               ]
    text = "These are top view points in Pattaya:"
    markup.add(*buttons)
    bot.send_message(chat_id=message.from_user.id,
                     text=text,
                     reply_markup=markup)


@bot.message_handler(commands=['temples'])
def sights_temples(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text='The Sanctuary Of Truth',
                                          url='https://maps.app.goo.gl/jrbzuZnBxuHbWsbCA'),
               types.InlineKeyboardButton(text='Big Buddha Temple',
                                          url='https://maps.app.goo.gl/Zb4g66XPDz8LPDe38'),
               types.InlineKeyboardButton(text='Phra Tamnak Mountain Viewpoint',
                                          url='https://maps.app.goo.gl/Kfk6gUwsGNUhfmx77'),
               types.InlineKeyboardButton(text='Wat Huay Yai',
                                          url='https://maps.app.goo.gl/p7s37kVn7RK9CeLF6'),
               types.InlineKeyboardButton(text='Khao Chi Chan Buddha',
                                          url='https://maps.app.goo.gl/Cw33fihRJFdNJydW6'),
               types.InlineKeyboardButton(text='Viharn Sien',
                                          url='https://maps.app.goo.gl/NfUCQiQqkN8NrURe9'),
               types.InlineKeyboardButton(text='Wat Yan Nasangwararam Woramahawihan',
                                          url='https://maps.app.goo.gl/bGyxLnxxmBp2RGkf8'),
               types.InlineKeyboardButton(text='Buddhist temple',
                                          url='https://maps.app.goo.gl/9rZSHmgvEzfMbooXA'),
               types.InlineKeyboardButton(text='Wat Yanasangwararam',
                                          url='https://maps.app.goo.gl/o3wYVTotGY7nxBmr8'),
               types.InlineKeyboardButton(text='Temple',
                                          url='https://maps.app.goo.gl/9R8rSZVEFPwNB4ZQ9'),
               types.InlineKeyboardButton(text='Ubosoth Wat Song Metta Wanaram',
                                          url='https://maps.app.goo.gl/UJjTvV3rWU2pDUXCA'),
               types.InlineKeyboardButton(text='Wat Khao Khanthamat',
                                          url='https://maps.app.goo.gl/doR1GZAeqfdJzX7VA'),
               types.InlineKeyboardButton(text='Wat Sattahip (Wat Luang Pho Yi)',
                                          url='https://maps.app.goo.gl/YbgAZuonz875B9KS7'),
               ]
    text = "These are temples around Pattaya:"
    markup.add(*buttons)
    bot.send_message(chat_id=message.from_user.id,
                     text=text,
                     reply_markup=markup)


@bot.message_handler(commands=['activities'])
def sights_activities(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text='Windsurfing Club',
                                          url='https://maps.app.goo.gl/Xn268yxqeBNyG2hb8'),
               types.InlineKeyboardButton(text='Ramayana Water Park',
                                          url='https://maps.app.goo.gl/FspyF7R8qWSk6hL88'),
               types.InlineKeyboardButton(text='Columbia Pictures Aquaverse',
                                          url='https://maps.app.goo.gl/hgmEQ1SKKP2buA1QA'),
               types.InlineKeyboardButton(text='Ko Lan Island',
                                          url='https://maps.app.goo.gl/C1bABSaEkCoubjFK9'),
               types.InlineKeyboardButton(text='Khram Yai Island',
                                          url='https://maps.app.goo.gl/Mb6QY6WtTvgs7Zv98'),
               ]
    text = "These are top activities in Pattaya:"
    markup.add(*buttons)
    bot.send_message(chat_id=message.from_user.id,
                     text=text,
                     reply_markup=markup)


@bot.message_handler(commands=['touristic'])
def sights_touristic(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text='The Sanctuary Of Truth',
                                          url='https://maps.app.goo.gl/jrbzuZnBxuHbWsbCA'),
               types.InlineKeyboardButton(text='Pattaya Tower',
                                          url='https://maps.app.goo.gl/UKk5NKxRUhtbCHb4A'),
               types.InlineKeyboardButton(text='Pattaya Floating Market',
                                          url='https://maps.app.goo.gl/d5hWtqVmJcEfE4zN9'),
               types.InlineKeyboardButton(text='Pattaya Walking Street',
                                          url='https://maps.app.goo.gl/ccF8PaUjUuDJAXjz8'),
               types.InlineKeyboardButton(text='Underwater World Pattaya',
                                          url='https://maps.app.goo.gl/Vc2G8FjyLPFKTzkB9'),
               types.InlineKeyboardButton(text='Legend Siam Pattaya',
                                          url='https://maps.app.goo.gl/7cfqcRVaf9cEBDb39'),
               types.InlineKeyboardButton(text='Nongnooch Tropical Garden Pattaya',
                                          url='https://maps.app.goo.gl/T3k52mzMuHPX4BK87'),
               types.InlineKeyboardButton(text='Viharn Sien',
                                          url='https://maps.app.goo.gl/NfUCQiQqkN8NrURe9'),
               types.InlineKeyboardButton(text='Ko Lan Island',
                                          url='https://maps.app.goo.gl/C1bABSaEkCoubjFK9'),
               types.InlineKeyboardButton(text='Khram Yai Island',
                                          url='https://maps.app.goo.gl/Mb6QY6WtTvgs7Zv98'),
               types.InlineKeyboardButton(text='Mini Siam',
                                          url='https://maps.app.goo.gl/LDmx6nrN8Dgxcup9A'),
               ]
    text = "These are top tourist places in Pattaya:"
    markup.add(*buttons)
    bot.send_message(chat_id=message.from_user.id,
                     text=text,
                     reply_markup=markup)


@bot.message_handler(commands=['shopping'])
def sights_shopping(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text='Terminal 21 Pattaya',
                                          url='https://maps.app.goo.gl/YrRNCjspYsLMcneMA'),
               types.InlineKeyboardButton(text='Central Pattaya',
                                          url='https://maps.app.goo.gl/bbo4GAez8KwTvZy16'),
               ]
    text = "These are shopping centers:"
    markup.add(*buttons)
    bot.send_message(chat_id=message.from_user.id,
                     text=text,
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
                 text="How can I help you? 🔎\n"
                      "If any problems contact 👨🏻‍💻[admin](tg://user?id=360841329)",
                 parse_mode="markdown")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Your message received and appreciated 🤝:\n '{message.text}'")


@bot.message_handler(content_types=['voice'])
def handle_docs_voice(message):
    bot.reply_to(message, f"Your voice message is received and will be processed by our AI 🤖!")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    bot.reply_to(message, f"Great picture 👍!")


@bot.message_handler(content_types=['sticker'])
def handle_docs_sticker(message):
    bot.reply_to(message, f"Your sticker is lovely ❤️!")


@bot.message_handler(content_types=['video'])
def handle_docs_audio(message):
    bot.reply_to(message, f"Gorgeous video 🥰️!")


if __name__ == "__main__":
    bot.infinity_polling()
