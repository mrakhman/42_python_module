from random import randint

def generator(text, sep=" ", option=None):
    '''
    Splits the text according to sep value and yield the substrings.
    `option` parameter precises if an action is performed to the substrings before it is yielded.
    options: shuffle, unique, ordered
    '''

    if not isinstance(text, str) or option not in [None, "shuffle", "unique", "ordered"]:
        return print("ERROR")

    if option == 'unique':
        words = list(dict.fromkeys(text.split(sep))) # can't use set() because it doesn't preserve order
    
    elif option == 'ordered':
        words = sorted(text.split(sep))
    
    elif option == 'shuffle':
        words = text.split(sep)
        shuffle_list(words)

    else:
        words = text.split(sep)

    for word in words:
        yield word


def shuffle_list(arr):
    for i in range(len(arr) - 1):
        rand_index = randint(0, len(arr) - 1)
        arr[i], arr[rand_index] = arr[rand_index], arr[i]

        
if __name__ == '__main__':
    option1 = "Le Lorem Ipsum est simplement du faux texte."
    option2 = 'one one two two three _'
    text = option2

    print('Option = default, separator = default:')
    for word in generator(text):
        print(word)
    print('----------\n')

    print('Option = None:')
    for word in generator(text, sep=" ", option=None):
        print(word)
    print('----------\n')

    print('Option = shuffle:')
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print('----------\n')

    print('Option = unique:')
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    print('----------\n')

    print('Option = ordered:')
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print('----------\n')

    print('Separator = "n":')
    for word in generator(text, sep="n"):
        print(word)
    print('----------\n')

    print('Invalid input:')
    for word in generator([6, 7, 3, 4], option="ordered"):
        print(word)
    for word in generator(4, option="ordered"):
        print(word)
    for word in generator(4, option="whatever"):
        print(word)
    print('----------\n')



