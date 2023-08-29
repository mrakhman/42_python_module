import sys


def whatis():
    '''Says if number is even, odd or zero'''
    args_len = len(sys.argv)

    if args_len < 2:
        return ''  # Error: Add one number

    if args_len > 2:
        return ('AssertionError: more than one argument is provided')

    num_str = sys.argv[1]

    try:
        num = int(num_str)
        if num == 0:
            return ("I'm Zero.")

        if num % 2 == 0:
            return ("I'm Even.")

        if num % 2 != 0:
            return ("I'm Odd.")

    except Exception:
        return ('Argument should be an integer')


print(whatis())
