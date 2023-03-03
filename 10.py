# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки б ыли повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

N = int(input('Введите количество монеток на столе:'))
count_0 = 0
count_1 = 0
for i in range(N):
    k = int(input())
    if k == 1:
        count_1 +=1
print(count_1 if count_1<N/2 else N-count_0)

# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
# if x == 0:
#     count_zero += 1
# else:
#     count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

