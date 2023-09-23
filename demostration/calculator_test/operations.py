import retry_or_finished


def sum_operation(first, second):
    print("Result: ", first + second)
    return retry_or_finished.retry_or_finished()


def minus_operation(first, second):
    print("Result: ", first - second)
    return retry_or_finished.retry_or_finished()


def multiply(first, second):
    print("Result: ", first * second)
    return retry_or_finished.retry_or_finished()


def divided(first, second):
    try:
        print("Result: ", first / second)
        return retry_or_finished.retry_or_finished()
    except ZeroDivisionError as e:
        print(f'ZeroDivisionError: {e}')
        return retry_or_finished.retry_or_finished()


def raising_to_a_power(first, second):
    print("Result: ", first ** second)
    return retry_or_finished.retry_or_finished()
