import requests
import json


# Используем Yandex translate api.
# Документация: https://tech.yandex.ru/translate/doc/dg/concepts/About-docpage/

api_key = 'trnsl.1.1.20180215T072655Z.85a3da116efded15.8db4596a413e61cd579dcb066a703b18769d54cb'
lang = 'ru-en'
text = 'Привет мир!'
res = requests.post(
    'https://translate.yandex.net/api/v1.5/tr.json/translate',
    params={'key': api_key, 'lang': lang, 'text': text}
)

print(res.content)

# Преобразуем полученый контент из json в dict

response_content = json.loads(res.content.decode('utf-8'))
print(response_content)

# Либо проще:

print(res.json())










