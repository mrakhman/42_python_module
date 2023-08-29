import sys

NESTED_MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/',
}


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def morse_code(str):
    '''Transforms given alphanumeric string to morse code'''
    res_str = ''
    for el in str:
        if el not in NESTED_MORSE:
            return "AssertionError: the arguments are bad. \
Only alphanumeric characters"
        res_str += NESTED_MORSE[el] + ' '
    return res_str[:-1]  # trim last space


@_guard_
def main():
    '''Main for tests and error handling'''
    args_len = len(sys.argv)
    if args_len != 2:
        print('AssertionError: the arguments are bad. Provide 1 string')
        return

    res = morse_code(sys.argv[1].upper())
    print(res)


if __name__ == "__main__":
    main()
