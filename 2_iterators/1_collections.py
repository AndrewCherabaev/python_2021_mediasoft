# Списки (list)
l = [1, 2, 3, 3]
# Срезы
l_2 = l[1:3][::-1]  # [0, 3)
print(l_2)
# Добавление элементов: по ключу, append, insert
l[2] = 0
l.append(10)
l.insert(1, 5)
print(l)
# Наличие значения, длина и количество элементов по условию, индекс
print(6 in l, len(l), l.count(3), l[0])

# Кортежи (tuple)
t = (1, 2, 3, 3)
not_tuple = (
    1
)
but_this_tuple = (1,)
# Наличие значения, длина и количество элементов по условию, индекс
print(
    1 in t,
    len(t),
    t.count(3),
    t[1]
)
# Множественное присваивание
""" Можно объявить кортеж без скобок """
t = 1, 2
x, y = 1, 0
""" синтаксис кортежа позоляет быстро поменять местами значения перемнных """
x, y = y, x
""" "забивочная переменная" - если не нужны данные """
ten, _ = [10, 20]
print(ten)


# Перечисления (set)
s = {1, 2}
# Добавление
s.add(3)
# Обновление
s.update({6, 7})
# Удаление
s.remove(3)
# Операции над множествами: union, intersection, difference, symmetric_difference
n_1 = {1, 2, 3}
n_2 = {3, 4, 5}
""" объединение множеств: {1,2,3,4,5} """
n_1.union(n_2)
""" пересечение множеств: {3} """
n_1.intersection(n_2)
""" разница относительного левого множества: {1,2} """
n_1.difference(n_2)
""" полная разница: {1,2,4,5} """
n_1.symmetric_difference(n_2)


# Словари (dict)
d = {
    'key': 'value',
    (1, 2): 'one and two'
}
"""
    ключом может быть любое иммутабельное/уикальное значение:
    int(), float(), complex(), bool(), str(), tuple(), object
"""
print(d[(1, 2)])
# объявление через dict(key=value)
""" в этом случае все ключи будут строками """
dict(
    key='value'
)
# Длина
print(len(d))
# Получение значения, безопасное получение значения
print(d['key'], d.get('value'))
# Проверка наличия !ключа!
print('key' in d)
# Ключи, значение, ключ-значение
print(
    d.keys(),
    d.values(),
    d.items()
)
