# Aryan Samuel
# arsamuel@ucsc.edu
# programming assignment 1
# The follwing program initiates a guesing game that
#   asks the player to guess a number created by the
#   program that is between 1 amd 10.

def main():
    print("I'm thinking of an integer, you have three guesses.")
    from random import randint
    y = randint(2,9)
    x = eval(input('Guess 1: Please enter an integer between 1 and 10: '))
    if x > y:
        print('Your guess is too big.')
    if x < y:
        print('Your guess is too small.')
    if x == y:
        print('You got it!')
        import sys
        sys.exit()
    x = eval(input('Guess 2: Please enter an integer between 1 and 10: '))
    if x > y:
        print('Your guess is too big.')
    if x < y:
        print('Your guess is too small.')
    if x == y:
        print('You got it!')
        exit()
    x = eval(input('Guess 3: Please enter an integer between 1 and 10: '))
    if x > y:
        print('Too bad. The number is:',y)
    if x < y:
        print('Too bad. The number is:',y)
    if x == y:
        print('You got it!')
        import sys
        sys.exit()

main()
