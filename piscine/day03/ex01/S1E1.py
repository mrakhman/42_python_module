from S1E9 import Character

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


class Baratheon(Character):
    '''Class representing Baratheon family'''
    def __init__(self, first_name, is_alive=True, eyes='brown', hair='dark'):
        '''Creates Baratheon family character with first_name and is_alive'''
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'Baratheon'
        self.eyes = eyes
        self.hair = hair

    def die(self):
        '''Method that kills a character by setting is_alive to false'''
        super().die()

    # The __str__ method in Python represents the class objects
    # as a string – it can be used for classes.
    # This method is also used as a debugging tool when the members
    # of a class need to be checked.
    def __str__(self):
        '''Returns a human-readable, or informal, \
string representation of an object'''
        txt = f'''First Name: {self.first_name}; Alive: {self.is_alive}'''
        return txt

    def __repr__(self):
        '''Returns a more information-rich, or official, \
string representation of an object'''
        txt = f'''Baratheon instance: {'{ '}first_name: {self.first_name}; \
is_alive: {self.is_alive}{' }'}'''
        return txt


class Lannister(Character):
    pass

    # decorator
    def create_lannister(bzzzz):
        pass


@_guard_
def main():
    '''Main for tests and error handling'''
    bb = Baratheon('Here')
    print(str(bb))
    print(repr(bb))
    print('\n-----------\n')

    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)


if __name__ == "__main__":
    main()
