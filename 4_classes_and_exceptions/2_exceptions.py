""""""
"""
Exceptions -- исключения.
Можно понимать как ошибки, возникающие во время работы кода.
Ошибки не являются фатальными и не всегда останавливают работу программы.
"""

# Существует большое кол-во стандартных исключений.
KeyError
# d = {'key': 1}
# d['key2']

ZeroDivisionError
# 1/0

TypeError
# print(1 + '123')


# Обработка ошибок.
x = 3
y = 3
d = {'key': 1}

try:
    print(1 / x)
    f = x + y
    print(d['key'])
except ZeroDivisionError:
    """
    Вызовется только в случае ZeroDivisionError исключения.
    """
    print('На 0 делить нельзя.')
except TypeError:
    """
    Вызовется только в случае TypeError исключения.
    """
    print('Невозможно сложить эти типы.')
except Exception as e:
    """
    Ловим и получаем объект ошибки
    """
    print(f"что-то пошло не так: {e}")
except:
    """
    Если сама ошибка нам по барабану
    НО! Стандарт PEP8 не рокемендует такой способ
    """
    print("ловим любую ошибку")
else:
    """
    Вызовется только в случае отсутвия исключения.
    """
    print('Ошибок не было.')
finally:
    """
    Вызовется всегда.
    """
    print('Все закончилось.')

"""Вызов ошибок."""
# raise RuntimeError('Вызванное исключение.')


"""
Пишем свои исключения
Все исключения должны быть наследованны от базового класса.
"""


class MyError(Exception):
    pass


class ErrorConvert(MyError):
    pass


class InavalidString(MyError):
    pass


def string_to_numbers(string):
    if not string:
        raise InavalidString('Пустая или не валидная строка.')

    result = []
    for w in string:
        try:
            result.append(int(w))
        # Отлавливаем все возникшие ошибки.
        except Exception:
            raise ErrorConvert('Ошибка конвертирования на символе: {}'.format(w))
    return result


try:
    res = string_to_numbers(None)
    res = string_to_numbers('')
    res = string_to_numbers('d1234')
    print(res)
except MyError as error:
    print('Моя ошибка {}'.format(error))
