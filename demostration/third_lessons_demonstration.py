# Методи str

# isspace() - https://www.w3schools.com/python/ref_string_isspace.asp
# isalpha() - https://www.w3schools.com/python/ref_string_isalpha.asp
# islower() - https://www.w3schools.com/python/ref_string_islower.asp
# isupper() - https://www.w3schools.com/python/ref_string_isupper.asp
# isdigit() - https://www.w3schools.com/python/ref_string_isdigit.asp
# isalnum() - https://www.w3schools.com/python/ref_string_isalnum.asp
# isdecimal() - https://www.w3schools.com/python/ref_string_isdecimal.asp
# istitle() - https://www.w3schools.com/python/ref_string_istitle.asp

# index() - https://www.w3schools.com/python/ref_string_index.asp
# ljust() - https://www.w3schools.com/python/ref_string_ljust.asp
# format() - https://www.w3schools.com/python/ref_string_format.asp
# find() - https://www.w3schools.com/python/ref_string_find.asp
# endswith() - https://www.w3schools.com/python/ref_string_endswith.asp
# count() - https://www.w3schools.com/python/ref_string_count.asp       !!!
# center() - https://www.w3schools.com/python/ref_string_center.asp
# casefold() - lower() - https://www.w3schools.com/python/ref_string_casefold.asp
# capitalize() - https://www.w3schools.com/python/ref_string_capitalize.asp


# 1. istitle(), title(), isspace(), upper()
# 2. isalpha(), isupper(), upper(), isalnum(), isdigit()
# 3. count(),isspace(), format()
# 4. format()
# --------------------------------------------------------------------------------------------------------------------

# name = input('Enter your name: ')
#
# if name.isspace():
#     print('Please, enter your name')
# else:
#     print(f'Your name is {name}')

# --------------------------------------------------------------------------------------------------------------------

# name = input('Enter your name: ')
#
# result = name.isalpha()
#
# if not result:
#     print('Please, enter your name')
# else:
#     print(f'Your name is {name}')

# --------------------------------------------------------------------------------------------------------------------


# name = input('Enter your name: ')
#
# result = name.islower()
#
# if not result:
#     print('Your name in upper case !')
# else:
#     print(f'Your name is {name}')
# --------------------------------------------------------------------------------------------------------------------

# name = input('Enter your name: ')
#
# result = name.isdigit()
#
# if result:
#     print('AttributeERROR: THIS IS NOT WORD')
# else:
#     print(f'Your name is {name}')

# --------------------------------------------------------------------------------------------------------------------

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# city = input('Enter your city: ')
#
# result = 'Hello,{}. Your age is {}. You live in {}'.format(name, age, city)
#
# print(result)
#
#
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# city = input('Enter your city: ')
#
# result = 'Hello,{0}. Your age is {1}. You live in {2}'.format(name, age, city)
#
# print(result)


# name = input('Enter your name: ')
# age = input('Enter your age: ')
# city = input('Enter your city: ')
#
# result = f'Hello,{name}. Your age is {age}. You live in {city}'
#
# print(result)

# --------------------------------------------------------------------------------------------------------------------


# txt = "Hello, And Welcome To My WORLD!"
#
# x = txt.casefold()
# y = txt.lower()
#
# print(x)
#
# print()
#
# print(y)

# --------------------------------------------------------------------------------------------------------------------


# txt = "artem, welcome to my world."
#
# x = txt.capitalize()
#
# print(x)