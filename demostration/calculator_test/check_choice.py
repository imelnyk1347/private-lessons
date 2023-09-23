import operations
import back_end


def check_choice(first, second):
    if back_end.choice == 1:
        return operations.sum_operation(first, second)

    if back_end.choice == 2:
        return operations.minus_operation(first, second)

    if back_end.choice == 3:
        return operations.multiply(first, second)

    if back_end.choice == 4:
        return operations.divided(first, second)

    if back_end.choice == 5:
        return operations.raising_to_a_power(first, second)
