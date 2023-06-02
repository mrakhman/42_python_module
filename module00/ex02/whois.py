import sys

def ex02():
    args_len = len(sys.argv)

    if args_len < 2:
        return('Add one number')
    
    if args_len > 2:
        return('Add only one argument')
    
    if not sys.argv[1].isdigit():
        return('Argument should be an integer')

    if sys.argv[1] == '0':
        return("I'm Zero.")

    num = int(sys.argv[1][-1])

    if num % 2 == 0:
        return("I'm Even.")
    
    if num % 2 != 0:
        return("I'm Odd.")
    
    return('')

print(ex02())
