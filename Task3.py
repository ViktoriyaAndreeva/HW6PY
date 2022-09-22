#Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки

# было
n = int(input('Введите число N:\t'))
numbers = {i:(1 + 1 / i) ** i for i in range(1, n+1)}
print(f'Последовательность чисел:{numbers}')
summa = 0
for i in numbers:
    summa += round(numbers[i], 3)
print(f'Сумма цифр последовательности равна:{summa}') 


#стало
n = int(input('Введите число N:\t'))
fc = lambda x: (1 + 1 / x) ** x
numbers = [fc(x) for x in range (1, n + 1)]
print(round(sum(numbers), 3))
