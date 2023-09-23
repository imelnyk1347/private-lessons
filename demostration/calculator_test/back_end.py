from start import calculator
import check_number_of_choice
import input_first_parameter


def input_choice():
    global choice
    choice = int(input('Select operation (+, -, *, / ): '))
    check_number_of_choice.check_number_of_choice(choice)
    return input_first_parameter.input_first_parameter()


calculator()
