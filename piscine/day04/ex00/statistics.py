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


# TODO: error handling, input validation


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

    def var(values):
        mean_value = mean(values)

        squared_difference = [(el - mean_value) ** 2 for el in values]
        variance = sum(squared_difference) / len(squared_difference)
        return variance
        

    def std(values):
        variance = var(values)
        stdandard_deviation = variance ** (1/2)
        return stdandard_deviation


    # if 'mean' in kwargs.values():
    #     print('mean:', mean(args))

    # if 'median' in kwargs.values():
    #     print('median:', median(args))

    if 'quartile' in kwargs.values():
        print('quartile:', quartile(args))

    # if 'std' in kwargs.values():
    #     print('std:', std(args))

    # if 'var' in kwargs.values():
    #     print('var:', var(args))


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

    # Percintiles aaaaa
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [1, 2, 3, 4, 5, 6]
    arr3 = [1, 42, 360, 11, 64]
    arr3 = [1, 11, 42, 64, 360]
    ft_statistics(*arr1, toto="mean", tutu="median", tata="quartile") # Q2 = 4;   Q1 = 2; Q3 = 6
    ft_statistics(*arr2, toto="mean", tutu="median", tata="quartile") # Q2 = 3,5; Q1 = 2; Q3 = 5
    print()

    method = 'inverted_cdf'
    print('25 + 75 quartile numpy', np.percentile(np.array(arr1), 25, method=method), np.percentile(np.array(arr1), 75, method=method))
    print('25 + 75 quartile numpy', np.percentile(np.array(arr2), 25, method=method), np.percentile(np.array(arr2), 75, method=method))

    print('25 + 75 quartile numpy', np.percentile(np.array(arr3), 25, method=method), np.percentile(np.array(arr3), 75, method=method))

    # Stdandatd deviation:
    # arr1 = [1, 2, 3, 4, 5, 6, 7]
    # arr2 = [1, 2, 3, 4, 5, 6]
    # ft_statistics(*arr1, toto="mean", tutu="median", tata="quartile", tete="std", titi="var")
    # ft_statistics(*arr2, toto="mean", tutu="median", tata="quartile", tete="std", titi="var")
    # print()
    # print(np.std(arr1), np.var(arr1))
    # print(np.std(arr2), np.var(arr2))

if __name__ == "__main__":
    main()
