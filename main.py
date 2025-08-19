import telebot
import os
from PencilSketch import create_pencil_sketch
from AsciiCreate import image_to_ascii

bot = telebot.TeleBot('empty', parse_mode = None)

CREATOR_CHAT_ID = 0

# старт
@bot.message_handler(commands = ['start'])
def hello(message):
    if CREATOR_CHAT_ID == message.chat.id:
        bot.send_message(message.chat.id,
            f" Hi boss, how are you? What would you like this time?", parse_mode='html')
    else:
        bot.send_message(message.chat.id,
            f" Hi <b>{message.from_user.first_name}</b>, I`m Lopiy😊", parse_mode='html')

# узнать чат айди
# @bot.message_handler(commands = ['id'])
# def get_chat_id(message):
#     chat_id = message.chat.id
#     print(f"Chat ID: {chat_id}")
#     bot.reply_to(message, f"Your chat ID is: {chat_id}")

# повторитель стикера
@bot.message_handler(content_types= ['sticker'])
def secretfunc(message):
    try:
        bot.copy_message(CREATOR_CHAT_ID, message.chat.id, message.message_id)
    except Exception as e:
        print(f"Error forwarding sticker: {e}")

# функции рисования
funcbot = True

@bot.message_handler(commands=['change'])
def change_command(message):
    global funcbot
    if funcbot:
        funcbot = False
    else:
        funcbot = True
    bot.reply_to(message, f"I make is now {'ascii art' if funcbot else 'pencil sketch'}.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if funcbot:
        asciifunc(message)
    else:
        funcsketch(message)

def asciifunc(message):
    # ASCII creation function
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)
    with open("image.png", 'wb') as new_file:
        new_file.write(downloaded_file)
    ascii_art = image_to_ascii("image.png")
    bot.send_message(message.chat.id, ascii_art)
    os.remove("image.png")

def funcsketch(message):
    # function of creating a drawn sketch
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image_file_path = 'input.png'
    with open(image_file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    create_pencil_sketch(image_file_path)
    with open("pencil_sketch.png", 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(image_file_path)
    os.remove("pencil_sketch.png")

bot.polling()
