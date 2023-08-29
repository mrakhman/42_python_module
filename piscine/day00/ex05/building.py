import sys
import string


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def text_analyzer(text=""):
    '''Takes a single string argument and displays the sums of
      its upper-case characters, lower-case characters,
     punctuation characters and spaces.
     '''
    if not text:
        print("What is the text to count?")
        text = input()

    if type(text) != str:
        print("AssertionError: argument is not a string")
        return

    upper_case_n = 0
    lower_case_n = 0
    punctuation_n = 0
    spaces_n = 0
    digits_n = 0

    for i in range(0, len(text)):
        if text[i] == ' ':
            spaces_n += 1

        elif text[i].islower():
            lower_case_n += 1

        elif text[i].isupper():
            upper_case_n += 1

        elif text[i] in string.punctuation:
            punctuation_n += 1

        elif text[i].isdigit():
            digits_n += 1

    res = f"""
    The text contains {len(text)} characters:
    - {upper_case_n} upper letters
    - {lower_case_n} lower letters
    - {punctuation_n} punctuation marks
    - {spaces_n} spaces
    - {digits_n} digits
    """

    print(res)


@_guard_
def main():
    '''Main for tests and error handling'''
    args_len = len(sys.argv)
    if args_len > 2:
        print("AssertionError: provide only one argument")
    elif args_len == 1:
        text_analyzer()
    else:
        text_analyzer(sys.argv[1])

    pass


if __name__ == "__main__":
    main()
