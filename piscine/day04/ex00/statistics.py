# TODO: rm!!
import statistics
import numpy as np

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
    # print(args)
    # print(kwargs)
    functions = ['mean', 'median', 'quartile', 'standard deviation', 'variance']

    def mean(values):
        return sum(values) / len(values)

    def median(values):
        values = sorted(values)
        med_index = len(values) / 2
        if med_index % 1 > 0:
            return values[int(med_index)]
        else:
            med_index = int(med_index)
            return (values[med_index] + values[med_index - 1]) / 2

    def quartile(values):
        values = sorted(values)
        Q1 = None
        Q3 = None

        # rank_Q1 = 25 / 100 * (len(values) + 1)

        # if rank_Q1 % 1 > 0:
        #     rank_Q1_int = int(rank_Q1)
        #     rank_Q1_fraction = rank_Q1 // 1
        #     Q1 = rank_Q1_fraction * (values[rank_Q1_int] - values[rank_Q1_int - 1]) + values[rank_Q1_int - 1]
        # else:
        #     Q1 = values[int(rank_Q1) - 1]

        if len(values) % 2 > 0:
            med = median(values)
            Q1 = (values[0] + med) / 2
            Q3 = (values[-1] + med) / 2
        
        else:
            print('med', median(values))
            values_middle = int((len(values)) / 2)
            list_Q1 = values[:values_middle]
            list_Q3 = values[values_middle:]
            print(list_Q1, list_Q3)
            Q1 = median(list_Q1)
            Q3 = median(list_Q3)

        return [Q1, Q3]
        # return Q1


    # if 'mean' in kwargs.values():
    #     print('mean:', mean(args))

    # if 'median' in kwargs.values():
    #     print('median:', median(args))

    if 'quartile' in kwargs.values():
        print('quartile:', quartile(args))


# @_guard_
def main():
    '''Main for tests and error handling'''
    # ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    # print('25 quartile numpy', np.percentile(np.array([1, 42, 360, 11, 64]), 25))
    # print('75 quartile numpy', np.percentile(np.array([1, 42, 360, 11, 64]), 75))
    # print('---------------------------------')
    # ft_statistics(1, 42, 360, 11, toto="mean", tutu="median", tata="quartile")
    # print('25 quartile numpy', np.percentile(np.array([1, 42, 360, 11]), 25))
    # print('75 quartile numpy', np.percentile(np.array([1, 42, 360, 11]), 75))

    # print('25 quartile numpy', np.percentile(np.array([1, 42, 360, 11, 64]), 25))
    # print('75 quartile numpy', np.percentile(np.array([1, 42, 360, 11, 64]), 75))

    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [1, 2, 3, 4, 5, 6]
    ft_statistics(*arr1, toto="mean", tutu="median", tata="quartile")
    ft_statistics(*arr2, toto="mean", tutu="median", tata="quartile")
    print()

    print('25 + 75 quartile numpy', np.percentile(np.array(arr1), 25), np.percentile(np.array(arr1), 75))
    print('25 + 75 quartile numpy', np.percentile(np.array(arr2), 25), np.percentile(np.array(arr2), 75))


if __name__ == "__main__":
    main()
