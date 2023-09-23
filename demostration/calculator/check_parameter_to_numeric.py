import retry_or_finished
import check_choice


def check_parameter_to_numeric(first_check_object, second_check_object):
    if not first_check_object.isnumeric():
        print(f'{first_check_object} is not a numeric')
        return retry_or_finished.retry_or_finished()

    if not second_check_object.isnumeric():
        print(f'{second_check_object} is not a numeric')
        return retry_or_finished.retry_or_finished()

    return check_choice.check_choice(float(first_check_object), float(second_check_object))
