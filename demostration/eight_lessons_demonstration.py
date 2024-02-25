def check_first_number(number):
    if type(number) == int:
        return number
    else:
        return int(number)


# def check_second_number(second_number):
#     if type(second_number) == int:
#         return second_number
#     else:
#         return int(second_number)


first_number = input('Enter your first number: ' )
second_number = input('Enter your first number: ' )

print(check_first_number(first_number) + check_first_number(second_number))
