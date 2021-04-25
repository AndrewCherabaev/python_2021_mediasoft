# https://habr.com/ru/post/161205/
"""
Основные типы данных
"""
int(), float(), complex(), bool(), str(), list(), tuple(), dict(), set()
"""
    NB! это не функции а конструкторы типов
"""


""" Целые числа """
int
a = 1

""" Числа с плавающей точкой """
float
b = 0.1

""" Комплексые числа (a + bi) """
complex
c = 1 + 2j

""" Булев тип """
bool
d = True or False

""" Строки """
str
e = 'str'
e = "str"
e = """
    str
"""

"""Тип "Пустое значение" """
None

""" Список """
list
f = [1, 3, 4, 5, 6, 7]

""" Кортеж - неизменяемый список """
tuple
g = (1, 2, 3)
""" Это не кортеж """
not_tuple = (1)
but_this_tuple = (1,)
also_tuple = 1, 2, 3, 4

""" Словарь """
dict
h = {
    'key': 'value',
    (12, 3): 'birthday'
}

""" Перечисление - храниит только уникальные значения"""
set
i = {1, 2, 3, 3, 4}
duplicates = [1, 2, 4, 4, 6, 6, 7]
""" Выведет список из уникальных элементов """
print(list(set(duplicates)))

""" Приведение одного типа к другому """
j = int(0.1)
""" Выведет ошибку """
test = int('12a')
h = float('0.1')
k = tuple([1, 2, 3])
k = set([1, 2, 3])

# Математические операции: +, -, *, /, //, %, **
1 + 2
3 - 0
4 * 5
10 / 2
""" Деление нацело """
10 // 3
""" Остаток от деления """
10 % 3
""" Возведение в степень """
1 ** 3

""" Форматирование строк """
name = 'vasya'
""" "Old C-style" вывода через % и флаги форматирования """
print('My name is %s' % (name,))  # ожидает tuple
print('My name is %(name)s' % {'name': name})  # ожидает dict

""" Метод строки 'format' """
print('My name is {}'.format(name))
""" Передача через именованный аргумент 'x' """
print('My name is {x}'.format(x=name))
""" Интерполяция строк Python 3.6+ """
print(f'My name is {name}')
# Отдельно можно почитать
#   https://realpython.com/python-string-formatting
#   https://docs.python.org/3/library/string.html#format-string-syntax


string_plus_string = 'asdf' + str(1) + 'ghjk'
""" Прямая конкатенация строк """
string_and_string = 'asdf' 'ghjk'
print(string_plus_string, string_and_string)

# Срезы в списках и строках
list_of_nums = [1, 2, 3, 4, 5, 6]
""" Вернет [3, 4, 5] """
print(list_of_nums[2:5])
""" Вернет 'list' """
print('list_of_nums'[0:4])
""" Вернет 'smun_fo_tsil' """
print('list_of_nums'[::-1])

""" Нет "falsify" значений, но... """
print(False == 0)  # True
print(True == 1)  # True
print(False == '')  # False
print(True == 10)  # False
"""
... из-за того что bool наследуется от целых чисел:
number.Integral
    - int()
    - bool()
... False равен 0, True равен 1
"""
# Иерархия типов в Python
#   https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy

""" Запрос ввода с клавиатуры """
name = input(">>> ")
print(name)
