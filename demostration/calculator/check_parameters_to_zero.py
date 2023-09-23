import check_parameter_to_numeric


def check_parameters_to_zero(first_check_object, second_check_object):

    if len(first_check_object) == 0:
        print('ValueError: first parameter must be not empty')
        exit()
        # FIXME: crash

    if len(second_check_object) == 0:
        print('ValueError: second parameter must be not empty')
        exit()
        # FIXME: crash
        # FIXME: zero check

    return check_parameter_to_numeric.check_parameter_to_numeric(first_check_object, second_check_object)
