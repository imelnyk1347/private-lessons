#  name = 'Artem'  # приклад статичної перемінної

# name = input('Enter your name, please: ')  # приклад динамічної перемінної
#
#
# if name == 'Artem':
#     print(f'Correct, your name is {name}')
# else:
#     print('No')
# ----------------------------------------------------------------------------------------------
# name = {}
# print(type(name))  # перевірка типу даних перемінної
# ----------------------------------------------------------------------------------------------

# dict example

# name = {
#     'key': 'this is some value bla-bla-bla',
#     'key_1': 'some test',
#     'key_2': 15,
#     'key_3': 19,
#     'key_5': 10.652
# }
#
# print(name['key_5'])
# ----------------------------------------------------------------------------------------------
                # 0  1  2  3        4           5
                #-6 -5 -4  -3         -2         -1
# name_for_list = [0, 1, 2, 'name', 'some name', 10.50]
# name_for_tuple = (15, 87, 'Artem', 'school', 'Ukraine', 10.2564)
# name_for_string = 'Artem'

# print(name_for_list[1:4])
# print(name_for_tuple[4:6])
# print(name_for_string[2:4])


# Дати домашку по зрізам)))

# print(name_for_list[-5:-2])  # від -2 до кінця
# print(name_for_tuple[-5:-2])
# print(name_for_string[-3:])

# ----------------------------------------------------------------------------------------------

# bool examples
# name = 'Artem'
#
# name_one = 'Vasyl'
#
# print(name is name)
# print(name_one is name_one)
# print(name is name_one)
# print(name_one is name)

# ----------------------------------------------------------------------------------------------
# 'Конкатенація' тобто додавання стрічок або додавання двох перемінних
# name = '50'
# name_1 = '50'
# print(name + name_1)


# дублювання

# name = 'Artem'
# print(name * 5)

# len

# name = 'Artem'
# print(len(name))


# index
#
# "name = 'Artem'

# print(name[0:2])
# print(name[:3])"


name = 'this is on lower case'
print(name.isupper())
print(name.islower())
print(name.split())
print(name.title())
