from work_with_text import default_menu_of_text_program
from culc.check_parameters_to_zero import check_parameters_to_zero
from menu import menu


def back_to_find_word_on_text():
    return find_word_on_text()


def find_word_on_text():
    """Search word"""
    result = user_text.find(word)

    if result == -1:
        print('No found')
        return information()
    print('Found')
    return information()


def get_word_from_user():
    global word
    word = input('Enter your searching word: ')
    check_word = get_word_from_user() if check_parameters_to_zero(word) == ('ValueError: parameter must be '
                                                                            'not empty') else ''
    return find_word_on_text()


def get_text_from_user():
    global user_text
    user_text = input('Setup your global text: ')
    check_user_text = get_text_from_user() if check_parameters_to_zero(user_text) == ('ValueError: parameter must be '
                                                                                      'not empty') else ''
    return get_word_from_user()


def information():
    message = int(input("""
     - if continue (press 1) 
     - go back to previous menu (press 2)
     - go back to default menu (press 3)
    Result: """))
    match message:
        case 1:
            return back_to_find_word_on_text()
        case 2:
            return default_menu_of_text_program.default_menu_of_text_program()
        case 3:
            return menu.default_menu()
