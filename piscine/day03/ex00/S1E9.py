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
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Init function to create character'''
        if is_valid_name(first_name) and is_valid_is_alive(is_alive):
            self.first_name = first_name
            self.is_alive = is_alive
        else:
            return

    @abstractmethod
    def die(self):
        '''Method that kills a character by setting is_alive to false'''
        self.is_alive = False


class Stark(Character):
    '''Inherits from Character. \
Class representing the Stark family'''
    def __init__(self, first_name, is_alive=True):
        '''Init function to create Stark family character'''
        super().__init__(first_name=first_name, is_alive=is_alive)
        # TODO: figure out how to inherit abstract method




@_guard_
def main():
    '''Main for tests and error handling'''
    # aaa = Character('aa', False)
    # print(aaa)
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
