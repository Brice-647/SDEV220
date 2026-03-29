def get_number(user_input):
    """
    Converts input to an integer.
    Raises ValueError if input is not valid.
    """
    return int(user_input)


def double_number(user_input):
    """
    Takes input, converts it, and doubles it.
    """
    num = get_number(user_input)
    return num * 2