# Объявление функций
def summa(a: int, b: int) -> int:
    """
    типизация не обязательна, python не ругается
    """
    return a + b


summa(1, 2)
summa('1', '2')  # ошибки не будет, будет '12'


# Функция без возвращаемого значения
def do_nothing():
    ...


do_nothing()  # Вернет None


# Значение по умолчанию
def with_default(x, y=2):
    print(x + y)


with_default(1)
with_default(10, 20)


# Не используйте изменяемые типы для значений по умолчанию
def add_to_list(l=[]):
    """
    при каждом вызове без передачи аргумента l будет уеличиваться на 1
    """
    l.append(1)
    print(l)


# None как значение по умолчанию
def add_to_list(l=None):
    if l is None:
        l = []
    l.append(1)
    print(l)


# Список агрументов, "распаковка" *args
def some_args(*args):
    print(type(args))  # <class 'tuple'>


# Список именованных аргументов, "распаковка" **kwargs
def some_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>


"""
Можно использовать вместе
"""


def fun(first, *args, **kwargs):
    print(first, args, kwargs)


"""
можно передать аргумент по его имени
"""
def full_name(name='', surname='', lastname=''):
    print(f'{name} {surname} {lastname}')


full_name(lastname='ivanov')  # '  ivanov'

"""
ОШИБКА! Нельзя указывать позиционные аргументы после передачи по имени
"""
fun(1, 2, key='value', l=[], 1)


# Функция как объект.
def summa(x, y):
    return x + y


def do_smth(arg1, arg2, fun):
    if callable(fun):
        return fun(arg1, arg2)
    return None


do_smth(1, 2, summa)  # 3


# Функции в питоне являются объектами. С функциями можно работать так же как и объектами.
def fn(a: int, b: int = 1, c: list = None):
    print(a, b, c)


print(
    fn.__name__,  # 'fn'
    fn.__class__,  # <class 'function'>
    fn.__code__,  # <code object fn at 0x7fa8f81ef030, file ".../3_functions/1_functions.py", line 93>
    fn.__annotations__,  # {'a': <class 'int'>, 'b': <class 'int'>, 'c': <class 'list'>}
    fn.__defaults__,  # (1, None)
)
