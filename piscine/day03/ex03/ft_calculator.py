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
    '''Calculator class does calculations (+-*/) of vector with a scalar'''
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        '''Adds number to vector'''
        # I could use that if the subject wasnt stupid
        # Because it returns a new array and does not edit array in place
        # res = list(map(lambda x: x + object, self.vector))
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        '''Multiplies vector by number'''
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        '''Substract number from vector'''
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        '''Divide vector by number'''
        if object == 0:
            print('Error: division by 0')
            return
        else:
            for i in range(len(self.vector)):
                self.vector[i] /= object
            print(self.vector)


@_guard_
def main():
    '''Main for tests and error handling'''
    v1 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = Calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    print("---")
    v3 / 0


if __name__ == "__main__":
    main()
