# Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *
from random import randint
number1 = randint(1, 10)
number2 = randint(1, 10)

sum_numbers = number1 + number2
print(f'Сумма чисел: {sum_numbers}')
product_numbers = number1*number2
print(f'Произвидение чисел: {product_numbers}')

flag = True
attempts = 1
while flag:
    if attempts <= 3:
        print(f'Попытка  {attempts} / 3')
        answer1 = int(input('Введите одно из чисел: '))
        answer2 = int(input('Введите второе число: '))
        if answer1 == number1 or answer1 == number2:
            if answer2 == number1 or answer2 == number2:
                print(f'Верно, Петя загадал числа {number1}, {number2}')
                flag = False
        attempts+=1
    else:
        print('Вы использовали все попытки, перезапустите код.')
        flag = False

