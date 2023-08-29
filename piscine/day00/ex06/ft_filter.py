def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def ft_filter(function, iterable):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    try:
        res = [el for el in iterable if function(el)]
        for el in res:
            yield el
    except Exception:
        print('Error occured, check input values')


@_guard_
def main():
    '''Main for tests and error handling'''
    def check_even(number):
        if number % 2 == 0:
            return True
        return False

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(list(ft_filter(check_even, numbers)))
    print(list(filter(check_even, numbers)))


if __name__ == "__main__":
    main()
