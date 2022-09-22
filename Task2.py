#Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11

from functools import reduce

# было
number = input('Введите число:\t')
summa = 0
for i in number:
    if '0' <= i <= '9':
        summa += int(i)
print(f'Сумма цифр числа равна:{summa}') 


# стало
n = input("Введите вещественное число: ").replace(',', '')
m = list(map(int, n))
print(f'Сумма цифр числа равна', reduce(lambda x, y: x + int(y), m))
