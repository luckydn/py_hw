# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_dol_x = int(input('Введите количество долек по горизонтали: '))
chocolate_dol_y = int(input('Введите количество долек по вертикали: '))
chocolate_dol_k = int(input('Сколько долек хотите отломить: '))

if ((chocolate_dol_x * chocolate_dol_y) % chocolate_dol_k == 0):
    print('Можно')
else:
    print('Нельзя')