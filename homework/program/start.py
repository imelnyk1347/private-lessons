from calculator import back_end


def calculator():
    print("""
          Hello user.\n 
          Select operation:
          1. Додавання. 
          2. Віднімання. 
          3. Множення. 
          4. Ділення. 
          5. Піднесення до степеня. \n
          """)

    return back_end.input_data()

