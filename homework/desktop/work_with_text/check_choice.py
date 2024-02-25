from culc.check_parameters_to_zero import check_parameters_to_zero
from menu.extreme_exit import extreme_exit
from work_with_text import default_menu_of_text_program
from work_with_text.intermediate import intermediate


def return_to_def_menu():
    return default_menu_of_text_program.default_menu_of_text_program()


def check_user_choice_from_default_menu_of_text_program(parameter):
    if parameter > 4:
        print(f"No correct number {parameter} of choices. Please try again.")
        return return_to_def_menu()
    if parameter == 0:
        return extreme_exit()
    else:
        return intermediate(parameter)


def check_user_parameter_on_zero(obj):
    if check_parameters_to_zero(str(obj)) == 'ValueError: parameter must be not empty':
        print("""
        ValueError: parameter must be not empty
        Please, choose . . . 
        """)
        return return_to_def_menu()

    return check_user_choice_from_default_menu_of_text_program(int(obj))
