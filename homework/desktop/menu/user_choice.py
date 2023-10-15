from culc.default_info import calculator
from work_with_text.default_menu_of_text_program import default_menu_of_text_program


def user_choice(params):

    if params == 1:
        return calculator()

    if params == 2:
        pass

    if params == 3:
        return default_menu_of_text_program()

    if params == 4:
        pass
