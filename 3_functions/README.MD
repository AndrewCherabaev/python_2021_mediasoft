# Курс Python 2021 Mediasoft
## 3. Функции

### Конспект:
- [Функции](./1_functions.py)
- [Декораты](./2_decorators.py)
- [Генераторы](./3_generators.py)
- [Лямбды](./4_lambdas.py)

### Доп чтение
- [Функции в Python (python.ru)](https://pythonru.com/osnovy/funkcii-v-python)
- [Декораторы в Python (перевод)](https://tproger.ru/translations/demystifying-decorators-in-python/) - есть немножко про функциональное программирование

### ДЗ

Написать декоратор для подсчета времени выполнения функции

Для получения времени внутри декоратора использовать
```python
import datetime

now = datetime.datetime.now().timestamp() # возвращает текущий таймштамп
```
