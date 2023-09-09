def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def ft_statistics(*args: object, **kwargs: object) -> None:
    '''
    Function that takes numbers and functions to apply and
    returns mean, median, quartiles, standard deviation and variance.
    Supported functions: 'mean', 'median', 'quartile', 'var', 'std'
    '''

    def mean(values):
        '''Calculates mean value'''
        return sum(values) / len(values)

    def median(values):
        '''Calculates median value'''
        values = sorted(values)
        med_index = len(values) / 2
        if med_index % 1 > 0:
            return values[int(med_index)]
        else:
            med_index = int(med_index)
            return (values[med_index] + values[med_index - 1]) / 2

    def quartile(values):
        '''Calculates Q1 and Q3 quartiles (25% and 75%)'''
        values = sorted(values)
        Q1 = None
        Q3 = None

        N = len(values)
        rank_Q1 = (N) / 4
        Q1 = values[int(rank_Q1)]

        rank_Q3 = 3 * (N) / 4
        Q3 = values[int(rank_Q3)]
        return [float(Q1), float(Q3)]

    def var(values):
        '''Calculates variance'''
        mean_value = mean(values)

        squared_difference = [(el - mean_value) ** 2 for el in values]
        variance = sum(squared_difference) / len(squared_difference)
        return variance

    def std(values):
        '''Calculates standard deviation'''
        variance = var(values)
        stdandard_deviation = variance ** (1/2)
        return stdandard_deviation

    # Input validation
    if len(args) == 0:
        print('Error: provide int values')
        return

    if not all(isinstance(arg, (int, float)) for arg in args):
        print('Error: args must be of type int or float')
        return

    if 'mean' in kwargs.values():
        print('mean:', mean(args))

    if 'median' in kwargs.values():
        print('median:', median(args))

    if 'quartile' in kwargs.values():
        print('quartile:', quartile(args))

    if 'std' in kwargs.values():
        print('std:', std(args))

    if 'var' in kwargs.values():
        print('var:', var(args))


@_guard_
def main():
    '''Main for tests and error handling'''
    ft_statistics(
        1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    ft_statistics('4', '5', 1, 3, toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
