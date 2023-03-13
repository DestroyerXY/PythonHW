# Задача 32: Определить индексы элементов массива (списка),
#  значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
Max = int(input('Введите максимум массива:'))
Min = int(input('Введите минимум массива:'))
array_1 = [random.randint(-100, 100) for _ in range(10)]
print(array_1)
array_2 = []
for i in range(len(array_1)):
    if Min < array_1[i] < Max:
        array_2.append(i)
print(array_2)
