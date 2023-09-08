def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


# def callLimit(limit: int):
#     '''Decorator that calls function limited number of times'''
#     count = 0
#     count = limit

#     def callLimiter(function):
#         '''Wrapper function, passes function to limit_function'''
#         def limit_function(*args: object, **kwds: object):  # aka wrapper
#             '''Function that calls a function under count number of times'''
#             nonlocal count
#             if count > 0:
#                 count -= 1
#                 return function(*args, **kwds)
#             print(f'Error: {function} call too many times')
#         return limit_function
#     return callLimiter


def callLimit(limit: int):
    '''Decorator that calls function limited number of times'''
    class Inner:
        '''Class that applies function and limit passed in callLimiter()'''
        def __init__(self, limit, function):
            self.count = limit
            self.function = function

        def limit_function(self, *args: object, **kwds: object):
            '''Method that calls function depending on call limit'''
            if self.count > 0:
                self.count -= 1
                return self.function(*args, **kwds)
            print(f'Error: {self.function} call too many times')

    def callLimiter(function):
        '''Function that calls limit_function method of Inner class'''
        lets_go = Inner(limit, function)
        return lets_go.limit_function

    return callLimiter


@_guard_
def main():
    '''Main for tests and error handling'''
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
