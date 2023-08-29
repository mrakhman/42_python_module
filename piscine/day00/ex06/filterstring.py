import sys
import string
from ft_filter import ft_filter


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def remove_punctuation(str):
    '''Removes ponctuation characters from string'''
    for char in str:
        if char in string.punctuation:
            str = str.replace(char, '')
    return str


def filter_string(str, n_chars):
    '''Returns a list of words of a string longer than given length'''
    str_arr = str.split()
    res = ft_filter(lambda el: len(el) > n_chars, str_arr)  # lambda
    res_res = [el for el in res]  # list comprehention
    return res_res


@_guard_
def main():
    '''Main for tests and error handling'''
    args_len = len(sys.argv)
    if args_len != 3 or not sys.argv[2].isdigit():
        return print("AssertionError: the arguments are bad. \
Usage: 2 arguments - string and integer")

    clean_str = remove_punctuation(str(sys.argv[1]))
    n_chars = int(sys.argv[2])

    res = filter_string(clean_str, n_chars)
    print(res)


if __name__ == "__main__":
    main()


# 'A, robo"t must protect its own existence as long as such protection \
# does not conflict with the First or Second Law ,,,,, . : $$$$' 9

# 'Hello the World' 4
