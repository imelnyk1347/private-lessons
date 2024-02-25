"""
    1. Написати скрипт (двома способами), який додаватиме дані в кортеж.
        Дані, які потрібно додати:
        example_file = (1, 2, 3, 4, 5, 6, 7)

    Приклад кортежу:
        corteg = ('apple', 'orange', 'banana', 'pineapple', 'kiwi', 'cherry', 'lemon')
"""
# corteg = ('apple', 'orange', 'banana', 'pineapple', 'kiwi', 'cherry', 'lemon')
#
# example_file = (1, 2, 3, 4, 5, 6, 7)
#
# corteg_ = list(corteg)
# corteg_.extend(example_file)
# print(tuple(corteg_))

# print(corteg + example_file)


"""
    2. Написати скрипт (двома способами), який оновить кортеж і замість 'kiwi' замінить на слово "EMPTY"

    Приклад кортежу:
        corteg = ('apple', 'orange', 'banana', 'pineapple', 'kiwi', 'cherry', 'lemon', 'kiwi')
"""
# cortege = ('apple', 'orange', 'banana', 'pineapple', 'kiwi', 'cherry', 'lemon', 'kiwi')
# cortege_ = list(cortege)
# cortege_[3], cortege_[7] = "EMPTY", "EMPTY"
# print(tuple(cortege_))

# cortege_ = []
# for i in cortege:
#     if i == 'kiwi':
#         i = "EMPTY"
#     cortege_.append(i)
#
# print(tuple(cortege_))

"""
    3. Написати скрипт (двома способами), який прийме на вхід кортеж в одному вигляді, а після обробки переверне 
       всі значення кортежу у зворотньому порядку в такому вигляді 
       ('kiwi', 'lemon', 'cherry', 'kiwi', 'pineapple', 'banana', 'orange', 'apple')

    Приклад кортежу:
        corteg = ('apple', 'orange', 'banana', 'pineapple', 'kiwi', 'cherry', 'lemon', 'kiwi')
"""
# corteg = ('apple', 'orange', 'banana', 'pineapple', 'kiwi', 'cherry', 'lemon', 'kiwi')
# new_cortege = []
# for element in corteg:
#     new_cortege.insert(0, element)
# print(tuple(new_cortege))


# first, second, third, *fourth = corteg
# fourth.reverse()
# fourth.append(third)
# fourth.append(second)
# fourth.append(first)
# print(tuple(fourth))

# corteg_ = list(corteg)
# corteg_.reverse()
# print(tuple(corteg_))

