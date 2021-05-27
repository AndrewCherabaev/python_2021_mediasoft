import requests

response = requests.get('https://academy.mediasoft.team/education/python/')


print(response.status_code)
print(response.content)
print(response.headers)


# https://gb.ru/posts
response = requests.post('https://geekbrains.ru/posts', params={'page': 2})
print(response.url)
print(response.status_code)
print(response.content)
print(response.headers)

