# Input validation
def is_valid_name(name):
    if not isinstance(name, str) or name == "":
        print("Error: name must be a string, not empty")
        return False
    return True

def is_valid_is_alive(is_alive):
    if not isinstance(is_alive, bool):
        print("Error: is_alive must be a boolean")
        return False
    return True


class GotCharacter:
    def __init__(self, first_name, is_alive = True):
        if is_valid_name(first_name) and is_valid_is_alive(is_alive):
            self.first_name = first_name
            self.is_alive = is_alive
        else:
            return


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        self.is_alive = False


if __name__ == '__main__':
    arya = Stark("arya")
    print(arya.__dict__)
    print(arya.__doc__)
    print("Arya is_alive:", arya.is_alive)
    arya.die()
    print("Arya is_alive:", arya.is_alive)
    arya.print_house_words()
