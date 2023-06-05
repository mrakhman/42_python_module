kata = (2019, 9, 25, 3, 30)  # 09/25/2019 03:30
# kata = (2019, 12, 5, 13, 3)  # 12/05/2019 13:03


def is_one_digit(n):
    return False if n // 10 > 0 else True


def format_number(n):
    return f"0{n}" if is_one_digit(n) else f"{n}"


if len(kata) != 5:
    print("Tuple needs to have 5 parameters: year, month, day, hour, minute")


else:
    m = format_number(kata[1])
    d = format_number(kata[2])
    y = format_number(kata[0])
    h = format_number(kata[3])
    min = format_number(kata[4])
    print(
        f"{m}/{d}/{y} {h}:{min}")
