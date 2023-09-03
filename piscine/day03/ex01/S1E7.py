from S1E9 import Character


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


def is_valid_hair(hair):
    '''Input validation for hair'''
    if not isinstance(hair, str):
        print("Error: hair must be a string")
        return False
    return True


def is_valid_eyes(eyes):
    '''Input validation for eyes'''
    if not isinstance(eyes, str):
        print("Error: eyes must be a string")
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
        if is_valid_name(first_name) and is_valid_is_alive(is_alive) \
                and is_valid_hair(hair) and is_valid_eyes(eyes):
            super().__init__(first_name=first_name, is_alive=is_alive)
            self.family_name = 'Baratheon'
            self.eyes = eyes
            self.hair = hair
        else:
            return

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
        txt = f'''First Name: {self.first_name}; Alive: {self.is_alive}; \
Family name: {self.family_name}; Eyes: {self.eyes}; Hair: {self.hair}'''
        return txt

    def __repr__(self):
        '''Returns a more information-rich, or official, \
string representation of an object'''
        txt = f"{vars(self)}"
        return txt


class Lannister(Character):
    '''Class representing Lannister family'''

    def __init__(self, first_name, is_alive=True, eyes='blue', hair='light'):
        '''Creates Baratheon family character with first_name and is_alive'''
        if is_valid_name(first_name) and is_valid_is_alive(is_alive) \
                and is_valid_hair(hair) and is_valid_eyes(eyes):
            super().__init__(first_name=first_name, is_alive=is_alive)
            self.family_name = 'Baratheon'
            self.eyes = eyes
            self.hair = hair
        else:
            return

    def die(self):
        '''Method that kills a character by setting is_alive to false'''
        super().die()

    def __str__(self):
        '''Returns a human-readable, or informal, \
string representation of an object'''
        txt = f'''First Name: {self.first_name}; Alive: {self.is_alive}; \
Family name: {self.family_name}; Eyes: {self.eyes}; Hair: {self.hair}'''
        return txt

    def __repr__(self):
        '''Returns a more information-rich, or official, \
string representation of an object'''
        txt = f"{vars(self)}"
        return txt

    @classmethod
    def create_lannister(
            cls, first_name, is_alive=True, eyes='blue', hair='light'):
        return cls(first_name, is_alive, eyes, hair)


@_guard_
def main():
    '''Main for tests and error handling'''
    # Find a solution so that "__str__" and "__repr__"
    # return strings and not objects
    Bar = Baratheon('Bar')
    print(str(Bar))
    print(repr(Bar))
    print('\n-----------\n')

    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)

    print("\n---\n")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)

    print("\n---\n")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, \
Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
