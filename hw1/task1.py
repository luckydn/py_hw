# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)



number = int(input('Введите трехзначное число: '))
if 99 < number < 1000:
    print(int(number/100)+int(number%10)+int((number%100)/10))
else:
    print('none')
