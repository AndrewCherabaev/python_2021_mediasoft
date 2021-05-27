# декоратор для подсчета времени выполнения функции

def time(func):
    def wrapper():
        import datetime
        begin=datetime.datetime.now().timestamp()  # возвращает таймштамп начала действия функции
        func()
        end=datetime.datetime.now().timestamp()    # возвращает таймштамп конца действия функции
        print('Время выполнения функции ')
        print(end - begin)
    return wrapper

@time
def hello_world():
    print('Hello world!')
    pow(2,200000000)

hello_world()