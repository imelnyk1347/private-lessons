from menu.user_choice import user_choice
from menu.check_user_choice import check_user_choice_from_default_menu


def default_menu():
    global menu_choice

    menu_choice = int(input("""
    Select program function:
    
    Calculator      (press 1)
    Work with files (press 2)
    Work with text  (press 3)
    Parser          (press 4)
    
    If you want break program, press 'N' (or 'n', or something another) !!! (Backlog)
    
    Result: """))

    check_user_choice_from_default_menu(menu_choice)

    return user_choice(menu_choice)
