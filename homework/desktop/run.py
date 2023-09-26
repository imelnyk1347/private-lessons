from menu.menu import default_menu


try:
    default_menu()
except ImportError as e:
    raise f'Something went wrong. Could not import user menu: {e}'
