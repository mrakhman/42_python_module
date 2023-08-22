def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def slice_me(family: list, start: int, end: int) -> list:
    '''Prints list shape and returns a slice of an array [start; end)'''
    # input validation: start, end
    if not isinstance(start, int) \
            or not isinstance(end, int):
        print('Error: start and end should be of type int')
        return

    # input validation: list type
    if not isinstance(family, list) \
            or not all(isinstance(el, list) for el in family):
        print('Error: family and all its elements must be of type list')
        return

    # input validation: family elements of the same size
    if not all(len(el) == len(family[0]) for el in family):
        print('Error: all elements of family must have the same length')
        return

    print('My shape is:', (len(family), len(family[0])))

    try:
        sliced = family[start:end]
        print('My new shape is:',  (len(sliced), len(sliced[0])))
        return sliced
    except (IndexError):
        print('Error: incorrect start and end')
        return


@_guard_
def main():
    '''Main for tests and error handling'''
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print('1.')  # correct
    print(slice_me(family, 0, 2))
    print()
    print('2.')  # correct
    print(slice_me(family, 1, -2))
    print()
    print('3.')  # correct
    print(slice_me(family, -4, -2))
    print()
    print('4.')  # error: incorrect start and end (start > end)
    print(slice_me(family, -1, -3))
    print()
    print('5.')  # error: incorrect start and end (start > end)
    print(slice_me(family, 2, 0))
    print()
    print('6.')  # error: incorrect start and end (start before end)
    print(slice_me(family, -2, 1))
    print()
    print('7.')  # error: start of wrong type
    print(slice_me(family, '1', 3))
    print()
    print('8.')  # error: end of wrong type
    print(slice_me(family, 1, '3'))
    print()
    print('9.')  # error: wrong type of family
    print(slice_me('family', 1, 3))
    print()

    print('10.')  # error: family element not of type list
    family1 = [[1.80, 78.4],
               '[2.15, 102.7]',
               [2.10, 98.5],
               [1.88, 75.2]]
    print(slice_me('family', 1, 3))
    print()

    print('11.')  # error: family elements not of the same size
    family1 = [[1.80, 78.4, 1],
               [2.15, 102.7],
               [2.10, 98.5],
               [1.88, 75.2]]
    print(slice_me(family1, 1, 3))
    print()


if __name__ == "__main__":
    main()
