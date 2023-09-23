import check_all_user_parameters
import input_second_parameter


def input_first_parameter():
    global first_number
    first_number = input('Enter your first number: ')
    if check_all_user_parameters.check_all_user_parameters(first_number) == 'ValueError: parameter must be not empty':
        print('ValueError: parameter must be not empty')
        return input_first_parameter()
    return input_second_parameter.input_second_parameter()
