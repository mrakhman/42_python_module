import string
import sys


def text_analyzer(text=""):
    '''
    Takes a single string argument 
    and displays the sums of its upper-case characters, lower-case characters, 
    punctuation characters and spaces.
    '''

    if not text:
        print("What is the text to analyze?")
        text = input()

    if type(text) != str:
        print("AssertionError: argument is not a string")
        return

    upper_case_n = 0
    lower_case_n = 0
    punctuation_n = 0
    spaces_n = 0

    for i in range(0, len(text)):
        if text[i] == ' ':
            spaces_n += 1

        elif text[i].islower():
            lower_case_n += 1

        elif text[i].isupper():
            upper_case_n += 1

        elif text[i] in string.punctuation:
            punctuation_n += 1

    res = f"""
    The text contains {len(text)} character(s):
    - {upper_case_n} upper letter(s)
    - {lower_case_n} lower letter(s)
    - {punctuation_n} punctuation mark(s)
    - {spaces_n} space(s)
    """

    print(res)


if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len > 2:
        print("Error: provide only one argument")
    elif args_len == 1:
        text_analyzer()
    else:
        text_analyzer(sys.argv[1])


# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
# text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
# text_analyzer(42)
# text_analyzer()
