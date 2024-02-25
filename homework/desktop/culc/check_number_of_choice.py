from culc import back_end
from menu.extreme_exit import extreme_exit
from menu import menu


def check_number_of_choice(user_operation_choice):

    if user_operation_choice == 0:
        return extreme_exit()

    if user_operation_choice == 6:
        return menu.default_menu()

    if user_operation_choice not in [i for i in range(1, 6)]:
        print(f"No correct number {user_operation_choice} of choices. Please try again.")
        return back_end.input_choice()
