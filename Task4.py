#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce

# было
n = list(map(str, input(f'Задайте список через пробел: ').split()))
print(f'Заданный список: {n}')

def summa(n):
    m = n[1::2]
    summa = 0
    for digit in m:
        if digit.isdigit():
            summa += int(digit)
    return summa
summa(n)
print(f'Сумма элементов списка, стоящих на нечётной позиции, равна:{summa(n)}')


# стало
list = list(map(int, input(f'Задайте список через пробел: ').split()))
list_filtered = list[1::2]
print(reduce(lambda x, y: x + y, list_filtered))


# или еще
n = range(0, 10)
print(sum(map(lambda x: x[1], filter(lambda x: x[0] % 2 == 1, enumerate(n)))))
