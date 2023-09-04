def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


class Calculator:
    '''Calculator class calculates (dot product, addition, substraction) \
of two vectors of the same size'''
    @classmethod
    def dotproduct(cls, v1: list[float], v2: list[float]) -> None:
        '''Calculates dot product of two vectors'''

        def multiply_two_lists(v1, v2):
            '''New list that is a product of two lists'''
            return [v1[i] * v2[i] for i, _el in enumerate(v1)]

        def list_sum(lst):
            '''Sum of list values, works like reducer'''
            res = 0
            for el in lst:
                res += el
            return res

        new_v = multiply_two_lists(v1, v2)
        res = list_sum(new_v)
        print('Dot product is:', res)

    @classmethod
    def add_vec(cls, v1: list[float], v2: list[float]) -> None:
        '''Calculates sum of two vectors'''
        res = [v1[i] + v2[i] for i, _el in enumerate(v1)]
        print('Add Vector is:', res)

    @classmethod
    def sous_vec(cls, v1: list[float], v2: list[float]) -> None:
        '''Substracts one vector from another'''
        res = [v1[i] - v2[i] for i, _el in enumerate(v1)]
        print('Sous Vector is:', res)


@_guard_
def main():
    '''Main for tests and error handling'''
    a = [5, 10, 2]
    b = [2, 4, 3]
    Calculator.dotproduct(a, b)
    Calculator.add_vec(a, b)
    Calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
