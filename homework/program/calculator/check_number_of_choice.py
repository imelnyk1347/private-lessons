import back_end


def check_number_of_choice(user_operation_choice):
    if user_operation_choice > 5:
        print(f"No correct number {user_operation_choice} of choices. Please try again.")
        return back_end.input_data()
