import back_end


def retry_or_finished():
    result_of_user_choices = input('If you want to retry press Y else N: ')
    if result_of_user_choices == 'Y':
        return back_end.input_choice()
    elif result_of_user_choices == 'N':
        print('Program finished. Thanks ;-) ')
        exit()
    else:
        print('No identifier command. Program was finished')
        exit()
