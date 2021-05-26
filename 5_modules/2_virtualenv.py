# Виртуальное окружение

# Варианты:
#   * https://docs.python.org/3/library/venv.html
#   * Установка https://virtualenv.pypa.io/en/stable/installation/
#
# Активация виртуального окружения:
#   source /path/bin/activate
#
# Установка пакетов:
#   https://packaging.python.org/tutorials/installing-packages/#installing-from-pypi

# Пример: pip install python-telegram-bot
# Доки по библиотеке https://github.com/python-telegram-bot/python-telegram-bot

# Вторая либа: pip install pytelegrambotapi
# Дока https://github.com/eternnoir/pyTelegramBotAPI

# requirements: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1
# pipreqs для генерации файла https://github.com/bndr/pipreqs
# Установка зависимостей из requirements.txt - pip install -r requirements.txt


import telebot

bot = telebot.TeleBot('token')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=5)
