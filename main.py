import telebot
import os
from PencilSketch import create_pencil_sketch
from AsciiCreate import image_to_ascii

bot = telebot.TeleBot('EMPTY', parse_mode = None)
# переменая для смены режима
funcbot = True

# команды бота 1 привенствие
@bot.message_handler(commands = ['start'])
def hello(message):
    bot.send_message(message.chat.id, f" Hi <b>{message.from_user.first_name}</b>,"
                                      " I`m Lopiy😊", parse_mode = 'html')
# команды бота 2 информация
@bot.message_handler(commands = ['help'])
def hello(message):
    bot.send_message(message.chat.id, " My name is Lopiy😊\n"
                                      "Send me a images and I'll try to make it into an ascii art, or a pencil sketch.🖼️")
    bot.send_message(message.chat.id, "/change - command, if you want to change the image processing option🔄")

# команды бота 3 изменения режима
@bot.message_handler(commands=['change'])
def change_command(message):
    global funcbot
    if funcbot:
        funcbot = False
    else:
        funcbot = True
    bot.reply_to(message, f"I make is now {'ascii art' if funcbot else 'pencil sketch'}.")

# оброботка текста
@bot.message_handler(content_types= ['text'])
def secretfunc(message):
    # bot.send_message(message.chat.id, " я хочу пиццы 🍕 ")
    """with open("ukraina.png", 'rb') as photo:
        bot.send_photo(message.chat.id, photo)"""
"""
# получение изображения и редактирование
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if funcbot:
        asciifunc(message)
    else:
        funcsketch(message)

def asciifunc(message):
    # Получаем информацию о файле из сообщения
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    # Скачиваем фото на сервер
    downloaded_file = bot.download_file(file_path)
    with open("image.png", 'wb') as new_file:
        new_file.write(downloaded_file)
    # Преобразуем фото в ASCII-арт
    ascii_art = image_to_ascii("image.png")
    # Отправляем ASCII-арт в чат
    bot.send_message(message.chat.id, ascii_art)
    os.remove("image.png")
def funcsketch(message):
    # Сохранение файла из сообщения
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image_file_path = 'input.png'
    with open(image_file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    # Обработка изображения
    create_pencil_sketch(image_file_path)
    # Отправка обработанного изображения
    with open("pencil_sketch.png", 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    # Удаление временных файлов
    os.remove(image_file_path)
    os.remove("pencil_sketch.png")
"""
bot.polling()