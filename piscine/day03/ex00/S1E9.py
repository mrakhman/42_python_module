from abc import ABC, abstractmethod


# Input validation
def is_valid_name(name):
    '''Input validation for first_name'''
    if not isinstance(name, str) or name == "":
        print("Error: name must be a string, not empty")
        return False
    return True


def is_valid_is_alive(is_alive):
    '''Input validation for is_alive'''
    if not isinstance(is_alive, bool):
        print("Error: is_alive must be a boolean")
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


class Character(ABC):
    '''Abstract class. Takes first_name and is_alive \
and changes the health state of the character'''
    def __init__(self, first_name, is_alive=True):
        '''Init '''
        pass
        # TODO: here

    @abstractmethod
    def sss():
        '''Method that'''
        pass


class Stark(Character):
    '''Inherots from Character.\
Class representing the Stark family'''
    def __init__(self, first_name=None, is_alive=True):
        '''Init '''
        # TODO: here
        pass


@_guard_
def main():
    '''Main for tests and error handling'''
    pass


if __name__ == "__main__":
    main()
