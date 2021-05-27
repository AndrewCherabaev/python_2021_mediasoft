from urllib.parse import urljoin
import pprint
import requests

# Импортируем ключик из файла environment.py который у вас будет свой
from environment import TOKEN

HOST = 'https://api.telegram.org'
URI = '/bot{token}/{method}'

"""
Получение данных о боте
"""
def get_me():
    method_name = 'getMe'

    # Просто собираем URL
    url = urljoin(HOST, URI.format(token=TOKEN, method=method_name))
    # Тоже самое что и:
    # url = HOST + URI.format(token=TOKEN, method=method_name)
    print(url)
    #
    response = requests.get(url)
    return response.json()


# result = get_me()
# pprint.pprint(result)


"""
Получить все последние сообщения
"""
def get_updates():
    method_name = 'getUpdates'

    url = urljoin(HOST, URI.format(token=TOKEN, method=method_name))
    # print(url)
    response = requests.get(url)
    return response.json()

# result = get_updates()
# # pprint.pprint(result)
# #
# messages = [m['message']['text'] for m in result['result']]
# pprint.pprint(messages)

"""
Получаем все обновления с учетом последнего обновления
"""
def get_updates(update_id=None):
    method_name = 'getUpdates'


    url = urljoin(HOST, URI.format(token=TOKEN, method=method_name))
    print(url)
    if not update_id:
        response = requests.get(url)
    else:
        response = requests.get(url, params={'offset': update_id})
    return response.json()


# result = get_updates()
# pprint.pprint(result)

# last_update_id = result['result'][-1].get('update_id')
# print(last_update_id)
# result = get_updates(last_update_id + 1)
# pprint.pprint(result)

from requests.exceptions import ReadTimeout

"""
Получаем все последние сообщения с таймаутом
"""
def get_updates(update_id=None):
    method_name = 'getUpdates'

    url = urljoin(HOST, URI.format(token=TOKEN, method=method_name))
    # print(url)
    if not update_id:
        response = requests.get(
            url, params={'timeout': 10}, timeout=10
        )
    else:
        response = requests.get(
            url, params={'offset': update_id, 'timeout': 10}, timeout=10
        )
    return response.json()


"""
Тело бота (генератор): получаем сообщения и выбрасываем их наружу
"""
def get_messages():
    next_update_id = None
    './file.txt'
    while True:
        try:
            result = get_updates(next_update_id)
        except ReadTimeout:
            continue

        for update in result.get('result', []):
            """
            Роутинг: на какое сообщение как реагировать
            """
            if 'message' in update:
                yield update['message']
            elif 'edited_message' in update:
                yield update['edited_message']
            else:
                print('Неизвестный апдейт')

        if result.get('result'):
            """
            сохраняем из последнего сообщения ID апдейта 
            чтобы в следующий раз читать начиная со следующего
            """
            next_update_id = result['result'][-1].get('update_id') + 1


for message in get_messages():
    pprint.pprint(message)
