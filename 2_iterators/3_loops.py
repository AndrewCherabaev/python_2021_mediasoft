# while
while not "boolean condition":
    print('infinite loop')
i = 10
while i > 0:
    i -= 1
    print(i)


# for
""" range возвращает генератор """
for i in range(0, 10, 2):
    print(i)
""" range(10) -> [0,1,2,3,4,5,6,7,8,9], вывести диапазон [0, 10) """
""" range(1, 10) -> [1,2,3,4,5,6,7,8,9], вывести диапазон [1, 10) """
""" range(2, 10, 2) -> [2,4,6,8], выести диапазон [2, 10) с шагом 2 """


# for in list, tuple, set
for l in [1, 2, 3]:
    print(l)
for t in (1, 2, 3):
    print(t)
for s in {1, 2, 3}:
    print(s)


# enumerate list
""" enumerate(1,2,3) -> enumerate object [(0,1), (1, 2), (2,3)] """
for i, v in enumerate([1, 2, 3]):
    print(f'{i}: {v}')


# for in dict
for k in {1: 2, 3: 4}:
    """ выведет 1, 3 """
    print(k)  #


# dict: keys, value, items
for key in {1: 2, 3: 4}.keys():
    """ dict_keys([1,2]) """
    print(f'{key}')
for value in {1: 2, 3: 4}.values():
    """ dict_values([2,4]) """
    print(f'{value}')
for k, v in {1: 2, 3: 4}.items():
    """ dict_items([(1, 2), (3,4)]) """
    print(f'{k}: {v}')


# bonus! for in string
string = "some string"
for c in string:
    """
        s
        o
        m
        e
        
        s
        t
        r
        i
        n
        g
    """
    print(c)


# bonus! for...else
l = [1, 2, 3, 4]
for i in l:
    """ for...else используется только если внутри for есть выход по условию (break) """
    break
else:
    print('nothing found')
