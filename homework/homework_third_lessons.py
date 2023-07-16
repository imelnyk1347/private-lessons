"""
1. Написати скрипт, який прийматиме речення.
   Наприклад, юзер вводить речення: "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.",
   а скрипт робить перевірку:
    - якщо всі слова розпочинаються з великої букви, то перевести всі слова в нижній регістр;
    - якщо слова розпочинаються з маленької букви, то перевести у верхній регістр;
    - якщо юзер взагалі нічого не введе, то буде виведено "InputError:nothing has been entered"

"""
# user_input = input("Please, enter the text: ")
#
# if len(user_input) == 0:
#     print('InputError:nothing has been entered!')
# elif not user_input.istitle():
#     print(user_input.title())
# elif user_input.istitle():
#     print(user_input.lower())
# else:
#     print('Error: unexpected result!')

# Артем, виправи помилки в коді )))

"""
2. Написати скрипт, який прийматиме на перевірку слово.
   Наприклад, юзер вводить 'SpaceX' і скрипт:
    - якщо всі символи в слові складаються із букв, то буде виведено "All characters are letters";
    - якщо всі символи  з великої букви, то повідомлення "All characters are letters" буде виведено повністю
      у верхньому регістрі;
    - якщо в слові будуть і символи літер і цифр, то буде виведено повідомлення 'A mixed data type was entered';
    - якщо будуть введені лише символи цифр, то буде виведено повідомлення 'Only numeric characters were entered';
    - якщо не буде нічого введено, то буде виведено "InputError:nothing has been entered"

"""
# word = input('Enter a word: ')
# if len(word) == 0:
#     print('InputError:nothing has been entered')
# elif word.isdigit():
#     print('Only numeric characters were entered')
# elif word.isupper():
#     print('All characters are letters'.upper())
# elif word.isalpha():
#     print('All characters are letters')
# elif word.isalnum():
#     print('A mixed data type was entered')
# else:
#     print('Error: unexpected result!')
"""
3. Написати скрипт, який виведе речення для юзера (приклад речення буде нижче) і дасть можливість юзеру ввести слово. 
    - якщо слово буде знайдено у тексті, то вивести і саме слово, і кількість його повторень;
    - якщо слово не буде знайдено у тексті, то вивести 'The search for the word "" was not found.', де
      у "" - вивести що саме було введено юзером;
    - якщо були введені самі пробіли, то вивести 'Incorrect search data';
    - якщо не буде нічого введено, то буде виведено "InputError:nothing has been entered".
    
    Текст , який буде виведено для юзера:
    
    'Україна має декілька історичних назв, що є частково або повністю тотожними.Україна має декілька історичних назв, що є частково або повністю тотожними'

"""
# text = 'Україна має декілька історичних назв, що є частково або повністю тотожними.Україна має декілька історичних ' \
#        'назв, що є частково або повністю тотожними'
# print(text)
#
# user_input = input('Enter word to search: ')
#
# if user_input.isspace():
#     print('Incorrect search data')
# elif text.count(user_input) == 0:
#     if user_input.isdigit():
#         print(f'The search for the digit "{user_input}" was not found.')
#         exit()  # Артем, спробуй дома написати скрипт з використанням данної функції
#     print(f'The search for "{user_input}" was not found.')
# elif text.count(user_input) > 0:
#     print(f'Find: "{user_input}". Count: {text.count(user_input)}')


# Артем, подивися, можливо в коді є якіст помилки або ж код можна покращити
"""
4. Програма прийматиме дані юзера на вхід: ім'я, прізвище, вік, місце проживання, кількість батьків і виводитиме 
   введену інформацію в такому вигляді: 'Ваші дані успішно прийнято. Ваше прізвище та ім'я ""., Ваше місце народження та
   фактичне проживання "", Ви маєте "" батьків.', де в "" - потрібно, щоб були підставлені відповідні дані введені 
   користувачем.
    
   - якщо ім'я користувача було введено лише літерами і з маленької букви, то скрипт має виводити ім'я з великої літери;
   - якщо прізвище користувача було введено лише літерами і з маленької букви, то скрипт має виводити прізвище 
     з великої літери;
   - якщо місце проживання користувача було введено лише літерами і з маленької букви, то скрипт має виводити 
     місце проживання з великої літери;
   - якщо вік було введено буквами, а не цифрою, то після основного повідомлення в кінці буде виведено таке речення:
     'Ваш вік "" та кількість батьків "" було введено літерами, будь ласка, в майбутньому введіть цифри' - 
      і в "" потрібно буде підставити що саме ввів буквами юзер;
   - якщо в ім'я, прізвище та місце проживання буде введено будь-що окрім літер - вивести повідомлення 
     'A mixed data type was entered';
   - якщо вік буде більший за 100 років та кількість батьків буде більше 2, то вивести 
     "InputError: incorrect input data";
   - якщо жодне поле не буде введено, то вивести "InputError:nothing has been entered"  

"""
# user_name = input("Enter user name: ")
# user_surname = input("Enter user surname: ")
# user_living = input("Enter user living: ")
# user_age = input("Enter user age: ")
# user_parents = input("Enter user parents: ")
#
#
# if len(user_name) == 0 and len(user_surname) == 0 and len(user_living) == 0 and len(user_age) == 0 \
#       and len(user_parents) == 0:
#     print('InputError:nothing has been entered')
#     exit()
# if user_name.isalpha() and user_surname.isalpha() and user_living.isalpha():
#     if user_name.islower() and user_surname.islower() and user_living.islower():
#         if not user_age.isdigit() and not user_parents.isdigit():
#             print(f'Ваші дані успішно прийнято. Ваше прізвище та ім\'я {user_name.title()} {user_surname.title()}, '
#                   f'Ваше місце народження та фактичне проживання {user_living.title()}, Ви маєте {user_parents.upper()} '
#                   f'батьків. \nВаш вік {user_age.upper()} та кількість батьків {user_parents.upper()} '
#                   f'було введено літерами, будь ласка, в майбутньому введіть цифри.')
#
#         if user_age.isdigit() and user_parents.isdigit():
#             user_age, user_parents = int(user_age), int(user_parents)
#             if user_age > 99:
#                 print(f'InputError: incorrect input data, user_age is {user_age}')
#                 exit()
#             if user_parents > 2:
#                 print(f'InputError: incorrect input data, user_parents is {user_parents}')
#                 exit()
#             print(f'Ваші дані успішно прийнято. Ваше прізвище та ім\'я {user_name.title()} {user_surname.title()}, '
#                   f'\nВаше місце народження та фактичне проживання {user_living.title()}, Ви маєте {user_parents} '
#                   f'батьків.')
# else:
#     print('TypeError: invalid parameters !')
