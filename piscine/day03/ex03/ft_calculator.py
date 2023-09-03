def is_valid_name(name):
    '''Input validation for first_name'''
    if not isinstance(name, str) or name == "":
        print("Error: name must be a string, not empty")
        return False
    return True


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
    '''Calculator class'''
    def __add__(self, object) -> None:
        ''''''

    def __mul__(self, object) -> None:
        ''''''

    def __sub__(self, object) -> None:
        ''''''

    def __truediv__(self, object) -> None:
        ''''''
        pass


@_guard_
def main():
    '''Main for tests and error handling'''
    pass


if __name__ == "__main__":
    main()
