import sys

def ex01():
    args_len = len(sys.argv)
    one_str = ""

    if args_len < 2:
        return('Add at least one argument')

    for i in range(1, args_len):
        one_str = one_str + ' ' + sys.argv[i]

    words_reverse = one_str[::-1].swapcase().split()

    return(' '.join(words_reverse))

print(ex01())

