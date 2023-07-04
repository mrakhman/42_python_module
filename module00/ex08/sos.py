import sys

morse_dict = {
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

def morse_code(str):
    res_str = ''
    for el in str:
        if el not in morse_dict:
            return("ERROR. Only alphanumeric characters")
        res_str += morse_dict[el] + ' '
    return res_str[:-1] # trim last space

def ex08():
    args_len = len(sys.argv)
    if args_len < 2:
        return print("ERROR. Usage: enter at least one string")
    
    full_str = ' '.join(sys.argv[1:])
    res = morse_code(full_str.upper())
    print(res)


ex08()
