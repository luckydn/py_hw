# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии. >

num_a = int(input("Введите число A: "))
num_b = int(input("Введите число B: "))

def degree(a, b):
    if b == 1:
        return a
    else:
        return a * degree(a, b-1)
    
print(degree(num_a, num_b))