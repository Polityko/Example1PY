# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает 
# все чётные числа от 1 до N.

numbers = int(input('Введите число: '))
for numbers in range (1, numbers+1):
    if numbers % 2 ==0:
        print(numbers, end=",")