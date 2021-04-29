# list comprehension
l = [1, 2, 3, 4, 5, 6, 7, 8]
""" вместо написания цикла """
squares = []
for i in l:
    squares.append(i ** 2)
""" используем  синтаксис "списочного выражения" """
squares = [x ** 2 for x in l]
print(squares)


# dict, set comprehension
""" вместо [1,2,3] может быть и set и tuple """
s = {x ** 2 for x in [1, 2, 3]}
print(s)
""" здесь важно помнить, что у словаря есть ключ и значение """
d = {k: v for k, v in enumerate([1, 2, 3])}
print(d)


# generators
""" generator object, а не кортеж """
t = (x for x in [1, 2, 3])
for i in t:
    print(i)

""" ничего не выведет, потому что это генератор, а генераторы запускаются только один раз """
for i in t:
    print(i)


# additional conditions: for if
nums = [1, 2, 3, 4]
""" вместо map и filter используем list comprehension с условием """
even = [x for x in nums if x % 2 == 0]
