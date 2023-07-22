# Integers. STRING special characters

# str

# http://ruslan.rv.ua/python-starter/strings/escapes.html

# n = 'This is first line.\nThis is second line'
# print(n)

#----------------------------------------------------------------

# n = 'This is new line\rThis is second line'
# print(n)

#----------------------------------------------------------------

# n = 'This is new line.\t\t\t\t\t\t\t\tThis is second line'
# print(n)

#----------------------------------------------------------------

# n = 'This is new line. This is second line\a'
# print(n)

#----------------------------------------------------------------

# n = 'This is new line.\'This is second line\''
#
# t = "This is new line.\"This is second line\""
#
# s = "This is new line.\\This is second line\\"
#
# print(n, t, s)
#
# print(n, t, s, sep='\n', end='\n')

#----------------------------------------------------------------

# integers

# http://ruslan.rv.ua/python-starter/vars_and_types/numbers.html#_2

# first_string = 11
# second_string = '1'
# print(second_string + second_string)
# print(first_string + first_string)
# print(first_string % 2)
# print(first_string ** 2)
# print(first_string + second_string)
# print(second_string / 100)
# print(second_string + 100)
# print(second_string * 100)

#----------------------------------------------------------------
# List/Array - []

# l = []
# print(type(l))

# append() -> https://www.w3schools.com/python/ref_list_append.asp
# clear() -> https://www.w3schools.com/python/ref_list_clear.asp
# copy() -> https://www.w3schools.com/python/ref_list_copy.asp
# count() -> https://www.w3schools.com/python/ref_list_count.asp
# extend() -> https://www.w3schools.com/python/ref_list_extend.asp
# index() -> https://www.w3schools.com/python/ref_list_index.asp
# insert() -> https://www.w3schools.com/python/ref_list_insert.asp
# pop() -> https://www.w3schools.com/python/ref_list_pop.asp
# remove() -> https://www.w3schools.com/python/ref_list_remove.asp
# reverse() -> https://www.w3schools.com/python/ref_list_reverse.asp
# sort() - https://www.w3schools.com/python/ref_list_sort.asp

#----------------------------------------------------------------

# різниця між append та insert

# fruits = ['apple', 'banana', 'cherry']
# fruits_1 = ['apple', 'banana', 'cherry']
#
# fruits.insert(1, "orange")
# fruits_1.append("orange")
#
# print(fruits)
# print(fruits_1)

#----------------------------------------------------------------
# різниця між clear та pop

# fruits = ['apple', 'banana', 'cherry']
# fruits_1 = ['apple', 'banana', 'cherry']
#
# fruits.pop(2)
# fruits_1.clear()
#
#
# print('This is how pop work: ', fruits)
# print('This is how clear work: ', fruits_1)

#----------------------------------------------------------------
# різниця між remove та pop

# fruits = ['apple', 'banana', 'cherry']
# fruits_1 = ['apple', 'banana', 'cherry']
#
# fruits.remove("cherry")
# fruits_1.pop(2)
#
# print(fruits)
# print(fruits_1)
#----------------------------------------------------------------


cars = ['Ford', 'BMW', 'Volvo']
cars_1 = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)
cars_1.sort()

print(cars)
print(cars_1)