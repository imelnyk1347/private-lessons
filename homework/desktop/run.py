from menu.menu import default_menu

try:
    default_menu()
except NameError as e:
    print(f'Could not import this function: {e}')
except KeyboardInterrupt:
    print('Someone stop program')
