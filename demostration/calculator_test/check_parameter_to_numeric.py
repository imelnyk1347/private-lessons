import retry_or_finished
import check_choice


def check_parameter_to_numeric(check_first_object, check_second_object):
    if not check_first_object.isnumeric():
        print(f'{check_first_object} is not a numeric')
        return retry_or_finished.retry_or_finished()

    if not check_second_object.isnumeric():
        print(f'{check_second_object} is not a numeric')
        return retry_or_finished.retry_or_finished()

    return check_choice.check_choice(float(check_first_object), float(check_second_object))
