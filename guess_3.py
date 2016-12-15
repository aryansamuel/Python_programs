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
    for i in range(3):
        x = eval(input('Guess '+str(i+1)+': Please enter an integer between 1 and 10: '))
        if x > y :
            print('Your guess is too big.')
        if x < y :
            print('Your guess is too small.')
        if x == y:
            print('You got it!')
            break
    if x != y:
        print('Too bad. The number is:',y)

main()
