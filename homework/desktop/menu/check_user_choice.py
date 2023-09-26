from culc.check_parameters_to_zero import check_parameters_to_zero
from menu import menu
from menu.user_choice import user_choice


def return_to_def_menu():
    return menu.default_menu()


def check_user_choice_from_default_menu(parameter):
    if parameter > 4:
        print(f"No correct number {parameter} of choices. Please try again.")
        return return_to_def_menu()


def check_parameter_on_numeric(check_obj):
    if not check_obj.isnumeric():
        print(f'{check_obj} is not a numeric')
        return return_to_def_menu()
    return user_choice(check_obj)


def check_user_parameter_on_zero(obj):
    if check_parameters_to_zero(obj) == 'ValueError: parameter must be not empty':
        print("""
        ValueError: parameter must be not empty
        Please, choose . . . 
        """)
        return return_to_def_menu()

    return check_parameter_on_numeric(obj)
