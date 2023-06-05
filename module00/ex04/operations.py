import sys


def ex04():
    args_len = len(sys.argv)
    if args_len > 3 or args_len == 2:
        return ("AssertionError: provide 2 arguments")
    if args_len == 1:
        return ("Usage: python operations.py <number1> <number2> \nExample: \n\tpython operations.py 10 3")
    if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        return ("AssertionError: only integers")

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    sum_ab = a + b
    difference = a - b
    product = a * b
    quotient = a / b if b != 0 else "ERROR (division by zero)"
    remainder = a % b if b != 0 else "ERROR (modulo by zero)"

    res = f"""
Sum: \t\t{sum_ab}
Difference: \t{difference}
Product: \t{product}
Quotient: \t{quotient}
Remainder: \t{remainder}
"""

    return res


print(ex04())
