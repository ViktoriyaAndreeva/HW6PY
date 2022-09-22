#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# было
from math import factorial

n = int(input('Введите число N:\t'))
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)
print(faktorial(n))        


# стало
def faktorial():

    factorial = lambda f : f * factorial(f-1) if f > 0 else 1
    print("Факториал заданного числа равен:", factorial(int(input('Введите число N:\t'))))

faktorial()
