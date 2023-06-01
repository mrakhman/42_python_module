import sys

args_len = len(sys.argv)
print(args_len)
if args_len > 2:
    for i in range(1, args_len):
        print(sys.argv[i], end = " ")

# input_string = input()

# words_reverse = input_string[::-1].swapcase().split()

# print(words_reverse.join())
