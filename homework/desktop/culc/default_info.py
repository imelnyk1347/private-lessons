from culc.back_end import input_choice


def calculator():
    print("""
    
          Calculator.
    
          Hello user.\n 
          Select operation:
          1. Додавання. 
          2. Віднімання. 
          3. Множення. 
          4. Ділення. 
          5. Піднесення до степеня. \n
          """)

    return input_choice()
