from culc.check_all_user_parameters import check_all_user_parameters
from culc.check_parameter_to_numeric import check_parameter_to_numeric
from culc import input_first_parameter as ifp


def input_second_parameter():
    global second_number
    second_number = input('Enter your second number: ')
    if check_all_user_parameters(second_number) == 'ValueError: parameter must be not empty':
        print('ValueError: parameter must be not empty')
        return input_second_parameter()
    return check_parameter_to_numeric(ifp.first_number, second_number)
