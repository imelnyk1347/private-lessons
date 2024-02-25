"""
    1. Написати скрипт, який шукатиме назву фрукту зі списку. Якщо фрукт буде знайдено, то програма виведе
       'Found'.

    Наприклад, юзер вводить "banana" і програма виводить: 'Found, banana !'

    Масив по якому потрібно шукати фрукт:
    fruits = ['apple', 'banana', 'orange', 'grape', 'pear', 'quince', 'watermelon', 'orange', 'grapefruit', 'lemon']

"""

fruits = ['apple', 'banana', 'orange', 'grape', 'pear', 'quince', 'watermelon', 'orange', 'grapefruit', 'lemon']
user_input = input('Enter: ')

for fruit in fruits:
    if user_input != fruit:
        continue
    else:
        print(f'Found, {user_input}', end=' !')


"""
    2*. Написати скрипт, який рахуватиме кількість ідентичних елементів в масиві ліста.

    Наприклад, юзер вводить "banana" і програма виводить: 'Found, 3 elements !', якщо нічого не буде знайдено,
    то буде виведено "Found, 0 elements !"

    Масив по якому потрібно шукати кількість ідентчиних фрукт:
    fruits = ['apple', 'banana', 'orange', 'grape', 'pear', 'quince', 'apple', 'watermelon', 'orange', 'apple', 
    'grapefruit', 'lemon', 'apple']

"""

fruits = ['apple', 'banana', 'orange', 'grape', 'pear', 'quince', 'apple', 'watermelon', 'orange', 'apple',
          'grapefruit', 'lemon', 'apple']
count_elemets = 0
user_input = input('Enter: ')

for fruit in fruits:
    if fruit != user_input:
        continue
    else:
        count_elemets += 1

print(f'Found, {count_elemets} elements', end=' !')

"""
    3. Написати скрипт, який буде перебирати елементи і зі списку і просумує лише парні цифри (тобто, 2, 4, 6, 8, 
       10 і так далі).


    Результат повинен був виводити: 1054


    Масив по якому потрібно перебирати цифри:
    integer_elements = [53, 98, 46, 27, 89, 105, 35, 62, 86, 64, 682, 49, 37, 14, 9, 2, 0]
"""

integer_elements = [53, 98, 46, 27, 89, 105, 35, 62, 86, 64, 682, 49, 37, 14, 9, 2, 0]

count_elements = 0
for integer in integer_elements:
    if integer % 2 == 0:
        count_elements += integer
    else:
        continue

print(count_elements)

"""
    4. Написати скрипт, який видалить усі дублікати чисел з масиву. 

    Результат виконання коду має бути таким: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    Приклад масиву з якого потрібно видалити дублікати:
    integer_elements = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

"""

integer_elements = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

unique_integer_elements = []

for integer in integer_elements:
    if integer not in unique_integer_elements:
        unique_integer_elements.append(integer)
    else:
        continue

print(unique_integer_elements)
