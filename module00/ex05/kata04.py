kata = (0, 4, 132.42222, 10000, 12345.67)
# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04


def is_one_digit(n):
    return False if n // 10 > 0 else True


def format_number(n):
    return f"0{n}" if is_one_digit(n) else f"{n}"


if len(kata) != 5:
    print("Tuple needs to have 5 parameters")

else:
    module = "module_" + format_number(kata[0])
    ex = "ex_" + format_number(kata[1])
    n1 = "{:.2f}".format(kata[2])
    n2 = "{:.2e}".format(kata[3])
    n3 = "{:.2e}".format(kata[4])

    res = f"{module}, {ex} : {n1}, {n2}, {n3}"
    print(res)
