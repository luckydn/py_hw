# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
min_elem = int(input("Введите минимальный эллемент: "))
max_elem = int(input("Введите максимальный эллемент: "))
new_list = []
index_elem_list = []
for i in range(20):
    new_list.append(randint(-50, 50))
    if max_elem > new_list[i] > min_elem:
        index_elem_list.append(i)
print(new_list)
print(index_elem_list)

