from S1E7 import Baratheon, Lannister


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


class King(Baratheon, Lannister):
    '''Class King that has getter and setter methods for eyes and hair'''

    def __init__(self, first_name):
        if is_valid_name(first_name):
            super().__init__(first_name=first_name)
        else:
            return

    # # First option: getter and setter methods
    def get_eyes(self):
        '''Eyes getter'''
        return self.eyes

    def get_hair(self):
        '''Hair getter'''
        return self.hair

    def set_eyes(self, eyes):
        '''Eyes setter'''
        self.eyes = eyes

    def set_hair(self, hair):
        '''Hair setter'''
        self.hair = hair

    # # # ----------------------------------------------------------
    # # # Second option: property() function
    # def get_eyes(self):
    #     return self._eyes

    # def get_hair(self):
    #     return self._hair

    # def set_eyes(self, eyes):
    #     self._eyes = eyes

    # def set_hair(self, hair):
    #     self._hair = hair

    # eyes = property(
    #     fget=get_eyes,
    #     fset=set_eyes,
    #     doc="The eyes property"
    # )

    # hair = property(
    #     fget=get_hair,
    #     fset=set_hair,
    #     doc="The hair property"
    # )

    # # # ----------------------------------------------------------
    # # # Third option: @property decorator
    # @property
    # def eyes(self):
    #     '''The eyes property'''
    #     return self._eyes

    # @eyes.setter
    # def eyes(self, value):
    #     self._eyes = value

    # @property
    # def hair(self):
    #     '''The hair property'''
    #     return self._hair

    # @hair.setter
    # def hair(self, value):
    #     self._hair = value


@_guard_
def main():
    '''Main for tests and error handling'''
    # First option:
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hair("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hair())
    print(Joffrey.__dict__)

    # # Second and third option (better):
    # Joffrey = King("Joffrey")
    # print(Joffrey.__dict__)
    # Joffrey.eyes = "blue"
    # Joffrey.hair = "light"
    # print(Joffrey.eyes)
    # print(Joffrey.hair)
    # print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
