import random

prompt = "What's your guess between 1 and 99?"
usage = '''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
'''

def ex09():
    number = random.randint(1, 99)
    n_attempts = 0
    print(usage)

    while True:
        guess = input()
        if guess == 'exit':
            print("Goodbye!")
            break

        if not guess.isdigit():
            print(f"That's not a number.\n{prompt}\n")
            n_attempts+= 1
            continue

        if int(guess) > number:
            print(f"Too high!\n{prompt}\n")
            n_attempts+= 1
            continue

        if int(guess) < number:
            print(f"Too low!\n{prompt}\n")
            n_attempts+= 1
            continue
        
        if int(guess) == number:
            n_attempts+= 1
            if (number == 42):
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if n_attempts == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print(f"You won in {n_attempts} attempts!")
            break

ex09()
