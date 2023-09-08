import random
import string
from dataclasses import dataclass, field


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Class that creates a student with fields \
name, surname, login, active, id'''
    name: string
    surname: string
    login: string = field(init=False)
    active: bool = True
    id: string = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        '''Methos that creates calculates value for login property'''
        self.login = self.name[0] + self.surname


@_guard_
def main():
    '''Main for tests and error handling'''
    student = Student(name="Edward", surname="agle")
    student2 = Student(name="maria", surname="rakhman", active=False)
    print(student)
    print(student2)

    # # Error case:
    # student = Student(name="Edward", surname="agle", login="toto")
    # student = Student(name="Edward", surname="agle", id="toto")
    # print(student)


if __name__ == "__main__":
    main()
