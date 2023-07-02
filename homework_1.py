"""

1. написати умову, яка буде перевіряти значення перемінної "obj = 25" на тип даних і виводитиме варіант відповіді в
   залежності від типу даних значення в такому вигляді "Типом даних перемінної 'obj' є <тут вказати тип даних>", якщо
   тип даних буде не відомий, то має бути виведено таке повідомлення "TypeError: Unknown type data"

"""
# obj = 25
# if type(obj) in (str, int, float, tuple, list, dict):
#     print(f"Типом даних перемінної 'obj' є {type(obj)}")
# else:
#     print("TypeError: Unknown type data")

"""

2. написати умову, яка буде перевіряти значення перемінної "name" (перемінна має бути динамічна) і перевіряти в списку 
   з іменами на наявність такого імені. Якщо ім'я буде знайдено в списку, то програма виведе повідомлення 
   "Your name is find", якщо ім'я не буде знайдено  - "Your name is not defined"
   
   Список по якому буде проводитися перевірка імені:
   
   list_of_names = [
    'Артем', 'Денис', 'Данііл', 'Данило', 'Олександр', 'Андрій', 'Богдан', 'Дмитро',
    'Нікіта', 'Микита', 'Назар', 'Кіріл', 'Кирило', 'Віктор', 'Віталій', 'Гліб',
    'Єгор', 'Іван', 'Ілля', 'Артур', 'Вадим', 'Тимофій', 'Михайло', 'Павло',
    'Микола', 'Євген', 'Сергій', 'Арсен', 'Юрій', 'Тимур', 'Давид', 'Марк',
    'Анна', 'Софія', 'Мілана', 'Злата', 'Дарина', 'Соломія', 'Вікторія', 
    'Анастасія', 'Дарія', 'Єва', 'Марія', 'Маргарита', 'Аделіна', 'Аліна', 'Поліна', 
    'Вероніка', 'Орися', 'Меланія', 'Діана', 'Яна', 'Анна', 'Любов', 'Катерина', 
    'Уляна', 'Олександра', 'Варвара','Sophia','Emily','Mary','Linda','Madison','Susan',
    'Lily','Michelle','Margaret','Tracy','Alice','Sandy','Rose','Grace','Allison',
    'Lucy','Mila','Cindy','Naomi','Jane','Hannah','Julie','Janet','Melanie','Stacy',
    'Sarah','Jake','Jack','Harry','Jacob','George','James','William','Connor','Joe',
    'Liam', 'Ethan','Richard','Michael','Justin','Parker','Matt','Luke','Neil',
    'Martin','Paul','John','Peter'
    ]

"""

# name = input('Please, enter your name: ')
#
# list_of_names = [
#     'Артем', 'Денис', 'Данііл', 'Данило', 'Олександр', 'Андрій', 'Богдан', 'Дмитро',
#     'Нікіта', 'Микита', 'Назар', 'Кіріл', 'Кирило', 'Віктор', 'Віталій', 'Гліб',
#     'Єгор', 'Іван', 'Ілля', 'Артур', 'Вадим', 'Тимофій', 'Михайло', 'Павло',
#     'Микола', 'Євген', 'Сергій', 'Арсен', 'Юрій', 'Тимур', 'Давид', 'Марк',
#     'Анна', 'Софія', 'Мілана', 'Злата', 'Дарина', 'Соломія', 'Вікторія',
#     'Анастасія', 'Дарія', 'Єва', 'Марія', 'Маргарита', 'Аделіна', 'Аліна', 'Поліна',
#     'Вероніка', 'Орися', 'Меланія', 'Діана', 'Яна', 'Анна', 'Любов', 'Катерина',
#     'Уляна', 'Олександра', 'Варвара', 'Sophia', 'Emily', 'Mary', 'Linda', 'Madison', 'Susan',
#     'Lily', 'Michelle', 'Margaret', 'Tracy', 'Alice', 'Sandy', 'Rose', 'Grace', 'Allison',
#     'Lucy', 'Mila', 'Cindy', 'Naomi', 'Jane', 'Hannah', 'Julie', 'Janet', 'Melanie', 'Stacy',
#     'Sarah', 'Jake', 'Jack', 'Harry', 'Jacob', 'George', 'James', 'William', 'Connor', 'Joe',
#     'Liam', 'Ethan', 'Richard', 'Michael', 'Justin', 'Parker', 'Matt', 'Luke', 'Neil',
#     'Martin', 'Paul', 'John', 'Peter'
# ]
#
# if name in list_of_names:
#     print('Correct')
# else:
#     print('No')

"""

3. програма має дві перемінні "first_number" і "second_number" ( перемінні динамічні - підказка, використати input() ): 
   написати умову, яка буде перевіряти суму двох перемінних і виводитиме повідомлення: 
   "Сума двох значень <тут потрібно буде виводити суму> знаходиться між 50 і 80"
   "Сума двох значень <тут потрібно буде виводити суму> менша за 120, але більша за 110"
   "Сума двох значень <тут потрібно буде виводити суму> більша за 100, але менша 109"
   "Сума двох значень <тут потрібно буде виводити суму> більша за 149, але менша за 200"
   
   Увага! Додаткова умова!!!!
   Якщо сума буде більша ніж указана в попередніх повідомленнях, то програма виводитиме:
   "Сума двох значень більша за 201 і становить <тут потрібно буде виводити суму>"
   
"""

# first_number = int(input('First: '))
# second_number = int(input('Second: '))
#
# third_number = first_number + second_number
#
# if 50 < third_number < 80:
#     print(f"Сума двох значень {third_number} знаходиться між 50 і 80")
# elif 120 > third_number > 110:
#     print(f"Сума двох значень {third_number} менша за 120, але більша за 110")
# elif 100 < third_number < 109:
#     print(f"Сума двох значень {third_number} більша за 100, але менша 109")
# elif 149 < third_number < 200:
#     print(f"Сума двох значень {third_number} більша за 149, але менша за 200")
# elif third_number > 201:
#     print(f"Сума двох значень більша за 201 і становить {third_number}")
# else:
#     print('ValueError')


"""

4.програма має список країн в перемінній "countries", і в динамічній перемінній прийматиме число від 1 до 45 і 
  в залежності від номеру числа шукатиме країну і виводитиме її назву. Якщо буде введено число більше 45 
  (наприклад, 46), то буде виведено повідомлення з помилкою - "Your choice is not correct !"  

  Перемінна countries:
  
  countries = {
    1: 'Ukraine',
    2: 'USA',
    3: 'Canada',
    4: 'United Kingdom',
    5: 'Germany',
    6: 'France',
    7: 'Italy',
    8: 'Spain',
    9: 'Australia',
    10: 'Japan',
    11: 'China',
    12: 'Russia',
    13: 'Brazil',
    14: 'Mexico',
    15: 'Argentina',
    16: 'India',
    17: 'South Korea',
    18: 'Netherlands',
    19: 'Switzerland',
    20: 'Sweden',
    21: 'Belgium',
    22: 'Norway',
    23: 'Denmark',
    24: 'Finland',
    25: 'Poland',
    26: 'Austria',
    27: 'Greece',
    28: 'Portugal',
    29: 'Ireland',
    30: 'New Zealand',
    31: 'Czech Republic',
    32: 'Turkey',
    33: 'Hungary',
    34: 'Thailand',
    35: 'Israel',
    36: 'Egypt',
    37: 'South Africa',
    38: 'Saudi Arabia',
    39: 'United Arab Emirates',
    40: 'Singapore',
    41: 'Malaysia',
    42: 'Indonesia',
    43: 'Vietnam',
    44: 'Philippines',
    45: 'Colombia'
}

"""

countries = {
    1: 'Ukraine',
    2: 'USA',
    3: 'Canada',
    4: 'United Kingdom',
    5: 'Germany',
    6: 'France',
    7: 'Italy',
    8: 'Spain',
    9: 'Australia',
    10: 'Japan',
    11: 'China',
    12: 'Russia',
    13: 'Brazil',
    14: 'Mexico',
    15: 'Argentina',
    16: 'India',
    17: 'South Korea',
    18: 'Netherlands',
    19: 'Switzerland',
    20: 'Sweden',
    21: 'Belgium',
    22: 'Norway',
    23: 'Denmark',
    24: 'Finland',
    25: 'Poland',
    26: 'Austria',
    27: 'Greece',
    28: 'Portugal',
    29: 'Ireland',
    30: 'New Zealand',
    31: 'Czech Republic',
    32: 'Turkey',
    33: 'Hungary',
    34: 'Thailand',
    35: 'Israel',
    36: 'Egypt',
    37: 'South Africa',
    38: 'Saudi Arabia',
    39: 'United Arab Emirates',
    40: 'Singapore',
    41: 'Malaysia',
    42: 'Indonesia',
    43: 'Vietnam',
    44: 'Philippines',
    45: 'Colombia'
}

number = int(input('Enter a number from 1 to 45: '))

for key, value in countries.items():
    if number > 45:
        print("Your choice is not correct !")
        break
    elif number != key:
        continue
    elif number == key:
        print(value)
