from culc import back_end
from culc.operations import sum_operation, minus_operation, multiply, divided, raising_to_a_power


def check_choice(first, second):
    if back_end.choice == 1:
        return sum_operation(first, second)

    if back_end.choice == 2:
        return minus_operation(first, second)

    if back_end.choice == 3:
        return multiply(first, second)

    if back_end.choice == 4:
        return divided(first, second)

    if back_end.choice == 5:
        return raising_to_a_power(first, second)
