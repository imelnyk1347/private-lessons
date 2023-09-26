from culc.check_number_of_choice import check_number_of_choice
from culc.input_first_parameter import input_first_parameter


def input_choice():
    global choice
    choice = int(input('''
                       Operations: 
                       1. +
                       2. -
                       3. *
                       4. /
                       5. **
                       
                       Back to default menu, press 6
                       
                       If you want break program, press 0
                       
                       
                       Operand: '''))
    check_number_of_choice(choice)

    return input_first_parameter()
