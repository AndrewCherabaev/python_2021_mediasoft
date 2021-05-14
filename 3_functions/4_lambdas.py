# Безымянные (анонимные) функции
l = lambda x: x**2
print(type(l))  # <class 'function'>

"""
Задачка с калькулятором может быть решена через лямбды
"""

# Создаем список доступных операций
ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

operator = '*'  # input("Введите оператор")

if operator in ops:
    ops[operator](1, 3)
"""
Или даже так (оператор ':=' доступен с Python 3.8)
"""
if op := ops.get(operator, None):
    op(1, 3)


