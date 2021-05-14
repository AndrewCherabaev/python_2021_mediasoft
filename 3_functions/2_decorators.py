# функция, которая принимает другую функцию в качестве аргумента
def summa(x, y):
    return x + y


def info(fn, *args, **kwargs):
    print(f'вызываем функцию {fn.__name__}')
    result = fn(*args, **kwargs)
    print(f'результат: {result}')
    return result


info(summa, x=1, y=2)


# Функция, которая оборачивает другую функцию
def print_info(fn):
    def wrapper(*args, **kwargs):
        print(f'вызываем функцию {fn.__name__}')
        result = fn(*args, **kwargs)
        print(f'результат: {result}')
        return result + 1

    return wrapper


printed = print_info(summa)
printed(10, 20)

"""
Или используем синтаксис @decorator чтобы не терять имя функции
"""
@print_info
def multiply(x, y):
    return x * y


multiply(2, 5)


# Декоратор с аргументами: декораторная фабрика
def if_more(arg_count):
    print('аргументы декоратора if_more')

    def decorator(fn):
        print(f'получили на вход функцию {fn.__name__}')

        def wrapper(*args, **kwargs):
            print('создали обертку с проверкой')
            if len(args) > arg_count:
                print(f'Число аргументов больше {arg_count}: {args}')
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@if_more(2)
def some_fn(*args):
    ...


some_fn(1, 2, 3, 4)


# Декоратор класса
def class_decorator(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'Object {instance} of {cls}')
        return instance

    return wrapper


@class_decorator
class MyClass:
    pass


MyClass()
