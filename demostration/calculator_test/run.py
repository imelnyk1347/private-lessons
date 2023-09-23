from culc.default_info import calculator


try:
    calculator()
except ImportError as e:
    raise f'Could not import calculator: {e}'
