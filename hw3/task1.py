# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
from random import randint
lenght_list = int(input('Введите длинну списка: '))
number_search = int(input('Введите число для поиска: '))
new_list = []
count = 0
for i in range(lenght_list):
    new_list.append(randint(0,100))
for i in range(len(new_list)):
    if new_list[i] == number_search:
        count+=1
print(new_list)
print(f'Количество повторений числа в списке: {count}')
if count == 0:
    min_range = 10000
    next_number = 0
    for i in range(len(new_list)):
        if (new_list[i] - number_search) < min_range:
            if (new_list[i] - number_search) < 0:
                min_range0 = ((new_list[i] - number_search)* -1)
                if min_range0 < min_range:
                    min_range = min_range0
                    next_number = new_list[i]
                    # print(f'+ = {min_range}, {next_number}')
            else:
                min_range = (new_list[i] - number_search)
                next_number = new_list[i]
                # print(f'- = {min_range}, {next_number}')
    print(f'Число "{next_number}", ближайшее к числу "{number_search}"')


