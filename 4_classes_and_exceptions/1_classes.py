""""""
"""
Класс - это
    - тип данных
    - шаблон объекта
    - описание данных
    - конструктор данных

Объект - экземпляр класса
"""


# Объявление класса
class Fruit:
    # атрибуты класса
    name = None
    color = None
    value = 1.0

    def __new__(cls, *args, **kwargs):
        """
        Конструктор объекта
        """
        return super().__new__(cls)

    def __init__(self, name, color):
        """
        Инициализатор объекта
        """
        self.name = name
        self.color = color

    def bite(self):
        """
        Метод без аргументов
        """
        if self.value > 0.0:
            self.value -= 0.3
            print('Укус на {}.'.format(0.3))
            return True

        return False

    def is_greater_then(self, amount):
        return self.value > amount


class Peel:
    has_peel = True

    def clean_out(self):
        self.has_peel = False


# В скобках указываем классы, от которых хотим наследоваться.
# Порядок наследования важен!!!

class Citrus(Peel, Fruit):
    # Переопределение родительского метода.
    def bite(self):
        if self.has_peel:
            print('Нужно сначала очистить')
            return
        # super -- вызовет метод у родителя.
        return super().bite()


lemon = Citrus(name='lemon', color='yellow')

lemon.bite()
lemon.clean_out()
lemon.bite()


# Магические методы. (Специальные методы)
# Методы класса, которы начинаются с __ и заканчиваются __
# и предоставляют возможость для взаимодействия с классом.


class Thing:

    def __init__(self, name):
        """
        Инициализация объекта
        """
        self.name = name

    def __str__(self):
        """
        Приведение к строке
        """
        return self.name

    def __add__(self, other):
        """
        Сложение вдух объектов типа Thing
        """
        return Thing(self.name + '-' + other.name)


print(Thing('some thing') + Thing('another thing'))


# Статические методы и методы класса
class DemonstrationClass:
    name = 'Name: '

    def __init__(self, name):
        self.name += name

    # Статический метод ничего не знает о классе и о объекте, к которому он принадлежит.
    @staticmethod
    def static_method():
        return 'Static method'

    # Метод класса знает все про класс и ничего не знает об объекте.
    @classmethod
    def class_method(cls):
        return f'Class property "name": `{cls.name}`'

    def instance_method(self):
        print(self.class_method())
        print(self.static_method())
        print(self.name)


DemonstrationClass('demo').instance_method()
