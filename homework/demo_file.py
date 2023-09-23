# def divided(first, second):
#     if second == 0 or first == 0:
#         return ValueError("Ділення на нуль не допускається")
#     return first / second
#
#
# def some_function():
#     return 'Some program on python'
#
#
# print(divided(0, 10))
#
# print()
#
# print(some_function())

# ----------------------------------------------------------------


# def divided(first, second):
#     if second == 0:
#         raise ValueError("Ділення на нуль не допускається")
#     return first / second
#
#
# def some_function():
#     return 'Some program on python'
#
#
# print(divided(10, 0))
#
# print()
#
# print(some_function())


# ----------------------------------------------------------------

def divided(parameter):
    try:
        with open(parameter, "r") as file:
            data = file.readline()
            file.close()
            return data
    except FileNotFoundError:
        return "Файл не знайдено"
    finally:
        print("End of function. ")


def some_function():
    return 'Some program on python'


print(divided("new_demo_file.txt"))

print()

print(some_function())

# ----------------------------------------------------------------


# def divided(first, second):
#     try:
#         num = int(first)  # catch ValueError exception
#         num_1 = int(second)  # catch ValueError exception
#         return num / num_1
#
#     except ValueError as e:
#         return f"ValueError: {e}"
#
#     except ZeroDivisionError as e:
#         return f"ZeroDivisionError: {e}"
#
#
# def some_function():
#     return 'Some program on python'
#
#
# first_param = input('Enter first parameter: ')
# second_param = input('Enter second parameter: ')
#
# print(divided(first_param, second_param))
#
# print()
#
# print(some_function())
