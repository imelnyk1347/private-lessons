"""
    Agenda

 1. Circles 'for' / 'while'
 2. range() ;  https://www.freecodecamp.org/ukrainian/news/tsykl-for-u-python-pryklad-syntaksysu/
 3. cirle for in list / string;
 4. break , continue in for / while circles ;
 5. pass()

 - presentation: https://docs.google.com/presentation/d/1qaukUA4OLjYnZgc1ylE_YqDrrvua5vsNlLMj2rmZwY4/edit?usp=sharing

 - for: https://www.w3schools.com/python/python_for_loops.asp ; https://www.freecodecamp.org/ukrainian/news/tsykl-for-u-python-pryklad-syntaksysu/

 - while: https://www.w3schools.com/python/python_while_loops.asp

 - loops inside loops: https://www.w3schools.com/python/gloss_python_for_nested.asp

 - range: http://ruslan.rv.ua/python-starter/loop_for/range.html

 - pass: https://www.w3schools.com/python/gloss_python_for_pass.asp

 - continue: https://www.w3schools.com/python/gloss_python_for_continue.asp

 - break: https://www.w3schools.com/python/gloss_python_for_break.asp

"""
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# for number in numbers:
#     pass

#1 спосіб виходу з циклу в самій умові while
# number = 0
# numbers = 15
# while number < numbers:
#     print(number)
#     number += 1
#
#
# number = 0
# while number < 15:
#     print(number)
#     number += 1
#
#
# number = 0
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# while number < len(numbers):
#     print(number)
#     number += 1

#2 спосіб виходу з циклу
# names = ['Ivan', 'Serhiy', 'Volodymyr', 'Artem', ' ']
# name = 'Artem'
# while True:
#     if name in names:
#         print('Found')
#         break
#     else:
#         print('Not found')
#         break

# Не запускай, бо зависне комп
# names = ['Ivan', 'Serhiy', 'Volodymyr', 'Artem', ' ']
# name = input('Enter you name: ')
#
# while True:
#     if name in names:
#         print('Found')
#     else:
#         print('Not found')
#
#
# print('OK')

#3 спосіб виходу з циклу

# names = ['Ivan', 'Serhiy', 'Volodymyr', 'Artem', ' ']
#
# name = 'Anton'
#
# iterations = True
#
# while iterations:
#     if name in names:
#         print('Found')
#         iterations = False
#     else:
#         print('Not found')
#         iterations = False
#
# print('OK')


# example = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for number in range(-100, -150, -1):
#     print(number)

# for number in range(1, len(example), 2):
#     print(number)


# example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#
# for number in example:
#     if number in (1, 2, 3, 4, 5, 6, 7):
#         continue
#     elif number == 8:
#         print('This is 8')
#     else:
#         break

# name = 10
# for i in range(1, 15, 2):
#   print(name * i)



# for i in range(4):
#     print(i)
#     print(i ** 2)
# print('Конец цикла')

# ----------------------------------------------------------------
# number = True
# while number:
#     name = input('Enter your name: ')
#     second_name = input('Enter second name: ')
#     if name != second_name:
#         print('False')
#     else:
#         print('True')
#         # number = False
#         # break
#
# print('End of circle while.')


# listeng = [1, 2, 3, 4, 5]
#
# i = 0
#
# while i < len(listeng):
#     if listeng[i] % 2 == 0:
#         print(listeng[i])
#     i += 1
#






# my_list = [1, 2, 3, 4, 5]
#
# i = 0
#
# while my_list[i] != 5:
#     print(my_list[i])
#     i += 1
#
# print('End of while circle.')
#
# for i in range(1, 5):
#     print(i)



#

# list_of_words = ["apple", "banana", "cherry"]
#
# for word in list_of_words:
#     print(word)
#
# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for list in list_of_lists:
#     sum = 0
#     for number in list:
#         sum += number
#     print(sum)
#
# list_of_lists = [[1, 2], [3, 4], [5, 6]]
#
# for list in list_of_lists:
#     print(list[0], list[1])
#
list_of_words = ["apple", "banana", "cherry", "orange", "lemon"]
fruits = ["apple", "banana", "cherry"]
for word in list_of_words:
    if word in fruits:
        print(word, "is a fruit")
    else:
        print(word, "is not a fruit")

# list_of_words = ["apple", "banana", "cherry", "orange", "lemon"]
# fruits = input('Enter fruit, please: ')
#
# for word in list_of_words:
#     if fruits != word:
#         print('Not found')
#     else:
#         print('True')
#         break

# Ітерація через список списків і виведення суми всіх чисел у кожному списку

# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for list_of_numbers in list_of_lists:
#     total = 0
#     for number in list_of_numbers:
#         total += number
#
# print(total)
#
# # Ітерація через список і перевірка, чи є кожне слово у списку "fruits"
#
# list_of_words = ["apple", "banana", "cherry", "orange", "lemon"]
# fruits = ["apple", "banana", "cherry"]
# for word in list_of_words:
#     if word in fruits:
#         print(word, "is a fruit")
#     else:
#         print(word, "is not a fruit")
#
# # Ітерація через список і додавання кожного слова до нового списку
#
# list_of_words = ["apple", "banana", "cherry"]
# new_list = []
# for word in list_of_words:
#     new_list.append(word)
#     print(new_list)

# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for list_of_numbers in list_of_lists:
#     total = 0
#     for number in list_of_numbers:
#         total += number
#         print(total, end=' ', sep='')
#         print()
#     print(total, end='\n')
#     print()
# print(total, end='\n')