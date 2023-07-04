import sys
import string

test = 'A, robo"t must protect its own existence as long as such protection does not conflict with the First or Second Law ,,,,, . : $$$$'

def remove_punctuation(str):
    for char in str:
        if char in string.punctuation:
            str = str.replace(char, '')
    return str

def filter_words(str, n_chars):
    str_arr = str.split()
    res = [word for word in str_arr if len(word) > n_chars] # list comprehension expression
    return(res)


def ex07():
    args_len = len(sys.argv)
    if args_len != 3 or not sys.argv[2].isdigit():
        return print("ERROR. Usage: 2 arguments - string and integer")
    
    clean_str = remove_punctuation(str(sys.argv[1]))
    n_chars = int(sys.argv[2])

    res = filter_words(clean_str, n_chars)
    print(res)

ex07()
