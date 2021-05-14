# Задача: range который возвращает ключ-значение
"""
Обычное генераторное выражение
"""
t = (x for x in [1, 2, 3] if x > 0)

"""
Дорогое решение: тратится много памяти
"""
l = list(range(10, 15, 2))
for i, v in enumerate(l):
    print(f'{i}: {v}')

"""
Решение через генераторы
"""
def key_value_range(*args):
    index = 0
    for k in range(*args):
        yield (index, k)  # вернуть ТЕКУЩЕЕ СОСТОЯНИЕ и ждать СЛЕДУЮЩЕГО ОБРАЩЕНИЯ
        index += 1


for idx, value in key_value_range(10, 15, 2):
    print(f'{idx}: {value}')

