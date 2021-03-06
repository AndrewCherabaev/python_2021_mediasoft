# Курс Python 2021 Mediasoft
## 2. Условия, циклы, итераторы

### Конспект:
- [Коллекции и операции над ними](./1_collections.py)
- [Условный оператор](./2_conditions.py)
- [Циклы](./3_loops.py)
- [Итераторы](./4_iterators.py)

### ДЗ
- **FizzBuzz** : 

Написать программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем, программа должна выводить слово `Fizz`, а вместо чисел, кратных пяти — слово `Buzz`. Если число кратно и 3, и 5, то программа должна выводить слово `FizzBuzz`.
    
Пример:   
```
7
8
Fizz      # вместо 9
Buzz      # вместо 10
11
Fizz      # вместо 12
13
14
FizzBuzz  # вместо 15
```

- **Ключ-значение** :
    
Написать программу, которая берет словарь и меняет местами ключи и значения. Попытаться реализовать за наименьшее кол-во строк.

Пример: 
```
{'name': 'ivan', 'surname': 'ivanov'} -> {'ivan': 'name', 'ivanov': 'surname'}
```

- **Дубликаты** :

Написать программу, которая берет исходный список и формирует новый список. В новом списке должны содержаться все элементы из исходного, за исключением дублей.

Пример: 
```
[1, 1, 2, 3, 5, 4, 5, 5, 6] -> [1, 2, 3, 5, 4, 6]
```