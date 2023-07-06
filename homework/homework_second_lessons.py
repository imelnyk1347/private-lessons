"""
1. Написати скріпт, який буде розділяти значення стрічки "This is amazing string" на окремі слова.
Наприклад:
програма отримує таке значення "This is amazing string" , а виведе ['This', 'is', 'amazing', 'string' ]

"""

"""
2. Написати скріпт, який шукатиме в значенні стріки "This is amazing string" окремі слова,
якщо слово не буде знайдено, то в консолі програма виведе повідомлення 'ValueError:parameter not found'

"""
# word = input("Please inter yur word: ")
#
# default_value = "This is amazing string"
#
# n = default_value.find(word)
#
# if n == -1:
#     print('ValueError:parameter not found')
# else:
#     print(f'Word "{word}" find on default value')

"""
3. Написати скріпт, який видалить із стрічки "    This is amazing string." усі пробіли.
Наприклад, 
програма приймає таке значення "                                         This is amazing string.                     ", 
в виведе "This is amazing string."
"""

# input_some_word = input("Please, input some word: ")
# print(input_some_word.strip(' '))

# name = input('Enter: some string: '.strip())
# print(name)


"""
4. Написати скріпт, який буде змінювати ім'я в перемінній my_awsome_string.
Наприклад, my_awsome_string = 'My name is Artem', а виведе 'My name is Volodymyr'

"""
# my_awsome_string = 'My name is Artem'
# print(my_awsome_string.replace('Artem', 'Volodymyr'))


"""
5.1. Написати скріпт, який буде ставити пробіл зліва і справа кожної букви.
Наприклад, some_string = 'Wolfeschlegelsteinhausenbergerdorff', 
а буде виведено 'W o l f e s c h l e g e l s t e i n h a u s e n b e r g e r d o r f f'

5.2 Написати скріпт , який об'єднає всі букви в одне слово.
Наприклад, some_string = 'Wolfeschlegelste', second_string = 'inhausenbergerdorff'
а виведе 'Wolfeschlegelsteinhausenbergerdorff'
"""
# some_string = input('Enter some word`s: ')
#
# print(' '.join(some_string))


# some_string = 'Wolfeschlegelste'
# second_string = 'inhausenbergerdorff'

# some_string = input('Enter your first word: ')
# second_string = input('Enter your second word: ')
#
# print(''.join([some_string, second_string]))

"""
6. Програма приймає будь-яке слово / або слова і виводить в консоль перші літери з великої букви.
Наприклад, приймає слово 'word', 'Word'. 

6.1. Програма приймає будь-яке слово / або слова і виводить в консоль всі літери з великої букви.
Наприклад, приймає слово 'word', 'WORD'. 

6.2. Програма приймає будь-яке слово / або слова і виводить в консоль всі літери з маленької букви. 
Наприклад, приймає слово 'WoRd', 'word'. 
"""
# 6.1
# first_example = input('Enter some text: ')  # or .title()
# print(first_example.title())  # or just print(first_example)

# 6.2
# first_example = input('Enter some text: ')  # or .upper()
# print(first_example.upper())  # or just print(first_example)

# 6.3
# first_example = input('Enter some text: ')  # or .lower()
# print(first_example.lower())  # or just print(first_example)
