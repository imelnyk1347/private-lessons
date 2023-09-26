from menu.user_choice import user_choice
from menu.check_user_choice import check_user_choice_from_default_menu


def default_menu():
    global menu_choice

    try:
        menu_choice = int(input("""
        Select program function:
        
        Calculator      (press 1)
        Work with files (press 2)
        Work with text  (press 3)
        Parser          (press 4)
        
        If you want break program, press 0
        
        Result: """))

        check_user_choice_from_default_menu(menu_choice)

        return user_choice(menu_choice)

    except ValueError as e:
        print(f"""
        
              Error: {e}. Введено не вірне значення.
               
              """)

        return default_menu()
