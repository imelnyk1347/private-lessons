from culc.check_number_of_choice import check_number_of_choice
from culc.input_first_parameter import input_first_parameter


def input_choice():
    global choice
    choice = int(input('Select operation (+, -, *, / ): '))
    check_number_of_choice(choice)
    return input_first_parameter()
