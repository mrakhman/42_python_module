def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    '''Calculates Body Mass Index based on height and weight'''

    # input validation: same length
    if len(height) != len(weight):
        print("Error: lists must be of the same size")
        return

    # input validation: type int or float
    for i, _ in enumerate(weight):
        if (not isinstance(weight[i], int)
            and not isinstance(weight[i], float)) \
            or (not isinstance(height[i], int)
                and not isinstance(height[i], float)):
            print("Error: all elements must be int or float")
            return

    # input validation: all  values > 0
    for el in height:
        if el <= 0:
            print('Error: height and weight cant be < 0')
            return

    bmi = [weight[i] / height[i] ** 2 for i, _ in enumerate(weight)]
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Shows if given BMIs (Body Mass Index) are above given limit'''
    # input validation for bmi
    for el in bmi:
        if not isinstance(el, int) and not isinstance(el, float):
            print("Error: all elements must be int or float")
            return

    # input validation for limit
    if not isinstance(limit, int) and not isinstance(limit, float):
        print("Error: limit must be int or float")
        return

    return [el > limit for el in bmi]


@_guard_
def main():
    '''Main for tests and error handling'''
    # Test give_bmi:
    # float
    height1 = [2.71, 1.15]
    weight1 = [165.3, 38.4]

    # int
    height2 = [2, 1]
    weight2 = [165, 38]

    # mix float and int
    height3 = [2, 1.15]
    weight3 = [165.3, 38]

    # wrong input: not float and not int
    height4 = ['aa', 1]
    weight4 = [165.3, True]

    # wrong input: different list length
    height5 = [2.71, 1.15, 4.0]
    weight5 = [165.3, 38.4]

    # wrong input: values <= 0
    height6 = [-10, 0]
    weight6 = [-165.3, 38.4]

    print('1. float, correct:')
    bmi1 = give_bmi(height1, weight1)
    print(bmi1, type(bmi1))
    print()

    print('2. int, correct:')
    bmi2 = give_bmi(height2, weight2)
    print(bmi2, type(bmi2))
    print()

    print('3. mix float and int, correct:')
    bmi3 = give_bmi(height3, weight3)
    print(bmi3, type(bmi3))
    print()

    print('4. wrong input: not float and not int, error:')
    bmi4 = give_bmi(height4, weight4)
    print(bmi4, type(bmi4))
    print()

    print('5. wrong input: different list length, error:')
    bmi5 = give_bmi(height5, weight5)
    print(bmi5, type(bmi5))
    print()

    print('6. wrong input: values <= 0, error:')
    bmi6 = give_bmi(height6, weight6)
    print(bmi6, type(bmi6))
    print()

    # Test apply_mpi:
    print('7.', bmi1, apply_limit(bmi1, 26))
    print()
    print('8.', bmi2, apply_limit(bmi2, 40.1))
    print()
    print('9.', [41.25, 38.0], apply_limit([41.25, 'aaa'], 40))
    print()
    print('10.', [41.25, 38.0], apply_limit([41.25, 38], '40'))


if __name__ == "__main__":
    main()
