# Подключение любого модуля из стандартной библиотеки.
# Как правило все используемые модули подключаются в начале файла.
# После подключения, получаем доступ для всех атрибутов модуля.
# Библиотека для выравнивания импортов - isort (pip install isort)
import datetime


# print(datetime.datetime.now())

# Получаем доступ к указанному атрибуту модуля
from datetime import timedelta

# print(datetime.datetime.now() - timedelta(days=7))

# Можно задать алиас для модуля. Используется для удобства работы с большими именами.
import random as rnd

# print(rnd.randint(1, 20))

# Можно импортировать несколько значений
from datetime import datetime, timedelta, timezone

# Импорт всех атрибутов модуля
from math import *

# print(pi, e, sin(1))

# Фаил __init__.py в каталоге говорит о том,
#  что все файлы в этом каталоге являются частью одного
#  модуля.

# В файле __init__.py может быть пустым
# или может определять основные "точки входа" в модуль.
import _function_module as f

# print(dir(f))

# решение импортов через __all__
# from django_example.models_in_one_file import User, Admin
# from django_example.models_file_by_class import User, Admin
# print(User, Admin)

# Важно помнить! Импортируемый файл всегда исполняется при импорте.
# from modules_5.functions import fib

# print(fib(3))


# Пути для импорта.
# import sys
# import pprint
#
# pprint.pprint(sys.path)
