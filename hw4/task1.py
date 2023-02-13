# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в 
# обоих наборах. Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# ======================================
# VAR 1
# ======================================

# len_sets_n = int(input('Введите длинну множества N: '))
# len_sets_m = int(input('Введите длинну множества M: '))
# sets_n = set()
# sets_m = set()
# for i in range(len_sets_n):
#     sets_n.add(int(input(f'Введите {i+1}/{len_sets_n} элемент множества N: ')))
# print(*sets_n)
# for i in range(len_sets_m):
#     sets_m.add(int(input(f'Введите {i+1}/{len_sets_m} элемент множества M: ')))
# print(*sets_m)
# crossings_sets = set()
# for i in sets_n:
#     for j in sets_m:
#         if i == j:
#             crossings_sets.add(j)
# print(*sorted(crossings_sets))


# ======================================
# VAR 2
# ======================================

len_sets_n = int(input('Введите длинну множества N: '))
len_sets_m = int(input('Введите длинну множества M: '))
sets_n = []
sets_m = []
for i in range(len_sets_n):
    sets_n.append(int(input(f'Введите {i+1}/{len_sets_n} эллемент множества N: ')))
print(*sets_n)
for i in range(len_sets_m):
    sets_m.append(int(input(f'Введите {i+1}/{len_sets_m} элемент множества M: ')))
print(*sets_m)
crossings_sets = set()
for i in sets_n:
    for j in sets_m:
        if i == j:
            crossings_sets.add(j)
print(*sorted(crossings_sets))


