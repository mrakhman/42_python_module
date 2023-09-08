def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def square(x: int | float) -> int | float:
    '''Returns squared value of given value'''
    return x * x


def pow(x: int | float) -> int | float:
    '''Returns exponentiation of given argument by himself'''
    return x ** x


# def outer(x: int | float, function) -> object:
#     '''Function that returns an object that when called returns 
# the result of the arguments calculation'''
#     count = x

#     def inner() -> float:
#         '''Function that applies function passed in outer()'''
#         nonlocal count
#         count = function(count)
#         return count

#     if not isinstance(x, int) and not isinstance(x, float):
#         print('Error: first parameter should be int or float')
#         return

#     if not callable(function):
#         print('Error: second parameter should be a function')
#         return

#     return inner

def outer(x: int | float, function) -> object:
    '''
    Function that returns an object that when called returns
    the result of the arguments calculation
    '''
    class Inner:
        '''Class that applies function passed in outer()'''
        def __init__(self, x):
            '''Init method, sets x value'''
            self.count = x

        def call(self):
            '''Call method, applies function passed from outer()'''
            self.count = function(self.count)
            return self.count

    if not isinstance(x, int) and not isinstance(x, float):
        print('Error: first parameter should be int or float')
        return

    if not callable(function):
        print('Error: second parameter should be a function')
        return

    return Inner(x).call


@_guard_
def main():
    '''Main for tests and error handling'''
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
