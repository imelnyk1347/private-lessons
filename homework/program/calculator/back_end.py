# from culc.default_info import calculator
from calculator.check_parameters_to_zero import check_parameters_to_zero
import check_number_of_choice


def input_data():

    global choice

    choice = int(input('Select operation (+, -, *, / ): '))

    check_number_of_choice.check_number_of_choice(choice)

    first_number = input('Enter your first number: ')

    second_number = input('Enter your second number: ')

    check_parameters_to_zero(first_number, second_number)

    # check_parameter_to_numeric.check_parameter_to_numeric(first_number, second_number)


# calculator()