# Курс Python 2021 Mediasoft
## 6. HTTP и работа с API

### Конспект:
- [Описание HTTP-протокола](./http.md)
  <hr>
- [Библиотека `requests`](./1_requests.py)
- [Работа со сторонним API](./2_api.py)
- [Работа с API Telegram](./3_telegram.py)


### Из официальной документации 
- [Telegram Bot API](https://core.telegram.org/bots/api)


### Требования к итоговому проекту
- в файле `README.MD` указать свои имя, фамилию и ссылку на бота: 
  `Иванов Иван. [bot](t.me/bot)`
- в файле `requirements.txt` указать все зависимости (генерируем через `pip freeze`)
- в файле `main.py` должен быть только запуск бота, все остальное - выделяем в модули
- в файле `.gitignore` добавить строчку `venv`
- токен авторизации можете не прикладывать, но если прикладываете,
  то используйте библиотеку [`python-dotenv`](https://pypi.org/project/python-dotenv/) и `.env`-файл для хранения токена