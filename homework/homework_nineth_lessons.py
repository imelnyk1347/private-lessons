"""
    1*. Написати скрипт, який виведе усі значення з дікта.
    Результат виконання коду:
    ['Ivan', 'Icshenko', '38', 'Lviv', 'FOP', 'MTS', '55000', '1300', 'Anhelina', '35', 'teacher', '40000', '1000', 'Anna', '8', 'pupil', 'Oleksandr', '10', 'pupil']


    Приклад дікта:
    var = {
        "name": "Ivan",
        "surname": "Icshenko",
        "age": "38",
        "living": "Lviv",
        "type_of_employment": "FOP",
        "job": "MTS",
        "month_salary_in_uah": "55000",
        "month_salary_in_usa": "1300",
        "family": {
            "wife": {
                "name": "Anhelina",
                "age": "35",
                "type_of_employment": "teacher",
                "month_salary_in_uah": "40000",
                "month_salary_in_usa": "1000",
            },
            "child1": {
                "name": "Anna",
                "age": "8",
                "type_of_employment": "pupil"
            },
            "child2": {
                "name": "Oleksandr",
                "age": "10",
                "type_of_employment": "pupil"
            }
        }
    }
"""

# var = {
#         "name": "Ivan",
#         "surname": "Icshenko",
#         "age": "38",
#         "living": "Lviv",
#         "type_of_employment": "FOP",
#         "job": "MTS",
#         "month_salary_in_uah": "55000",
#         "month_salary_in_usa": "1300",
#         "family": {
#             "wife": {
#                 "name": "Anhelina",
#                 "age": "35",
#                 "type_of_employment": "teacher",
#                 "month_salary_in_uah": "40000",
#                 "month_salary_in_usa": "1000",
#             },
#             "child1": {
#                 "name": "Anna",
#                 "age": "8",
#                 "type_of_employment": "pupil"
#             },
#             "child2": {
#                 "name": "Oleksandr",
#                 "age": "10",
#                 "type_of_employment": "pupil"
#             }
#         }
#     }
# local_var = []
#
# for value in var.values():
#     if type(value) == str:
#         local_var.append(value)
#
#     if type(value) == dict:
#         for v in value.values():
#             for new_val in v.values():
#                 local_var.append(new_val)
#
# print(local_var)

"""
    2. Написати трьома способа скрипт, який витягне всі ключі з дікта
    Результат виконання срипта має бути завжди таким:
    ['name', 'surname', 'age', 'living', 'type_of_employment', 'job', 'month_salary_in_uah', 'month_salary_in_usa']



        Приклад дікта:
    var = {
        "name": "Ivan",
        "surname": "Icshenko",
        "age": "38",
        "living": "Lviv",
        "type_of_employment": "FOP",
        "job": "MTS",
        "month_salary_in_uah": "55000",
        "month_salary_in_usa": "1300"
    }
"""
var = {
    "name": "Ivan",
    "surname": "Icshenko",
    "age": "38",
    "living": "Lviv",
    "type_of_employment": "FOP",
    "job": "MTS",
    "month_salary_in_uah": "55000",
    "month_salary_in_usa": "1300"
}
# 1
# list_for_dict = []
# for key in var.keys():
#     list_for_dict.append(key)
# print(list_for_dict)

# 2
# list_for_dict = var.keys()
# print(list(list_for_dict))

# 3
# list_for_dict = [i for i in var.keys()]
# print(list_for_dict)

"""
    3*. Написати скрипт, який перевірятиме значення на правильність написання і якщо 
       значення не правильно написано, то його потрібно видалити.

       Результат роботи скрипта:   
       {'France': 'Paris', 'Germany': 'Berlin', 'Japan': 'Tokyo', 'Poland': 'Warsaw'}


    Приклад дікта:
    countries_capitals = {
    "Ukraine": "Kivy",
    "USA": "Weshinton, P.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Poland": "Warsaw",
    "United Kingdom": "Lomdon"
}
"""
capitals = ["Kyiv", "Washington, D.C.", "Paris", "Berlin", "Tokyo", "Warsaw", 'London']

countries_capitals = {
    "Ukraine": "Kivy",
    "USA": "Weshinton, P.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Poland": "Warsaw",
    "United Kingdom": "Lomdon"
}

exam_dict = {}
for key, value in countries_capitals.items():
    if value in capitals:
        exam_dict[key] = value

print(exam_dict)

