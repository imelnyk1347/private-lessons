from culc import back_end


def retry_or_finished():
    result_of_user_choices = input('If you want to retry press Y else N: ')
    if result_of_user_choices in ('Y', 'y', 'yes', 'ok', 'OK', 'Ok', 'okay', 'Okay'):
        return back_end.input_choice()
    elif result_of_user_choices in ('N', 'n', 'no'):
        print('Program finished. Thanks ;-) ')
        quit()
    else:
        print('No identifier command. Program was finished')
        quit()
