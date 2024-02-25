from work_with_text.check_choice import check_user_parameter_on_zero


def default_menu_of_text_program():

    global text_menu

    try:
        text_menu = int(input("""
        
        Work with text.
        
        Select program function:
        
        1. Find word from your text
        2. Replace word on text
        3. Count words on text
        4. Counting letters on text
        
        
        Result: """))
        return check_user_parameter_on_zero(text_menu)
    except ValueError as e:
        print(f"""
        
              Error: {e}. Введено не вірне значення.
               
              """)
        return default_menu_of_text_program()
    except KeyboardInterrupt:
        print('Someone stop program')
