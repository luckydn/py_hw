# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите число: '))
degree = 1
flag = True
while flag:
    print(degree)
    degree *=2
    if degree > number:
        flag = False