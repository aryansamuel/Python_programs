# Aryan Samuel
# arsamuel@ucsc.edu
# prgramming assignment 6
# The following program asks the user for a jumbled word,
# then unjumbles and prints it.
# Note: The unjumbled word should be in the dictionary that is read by the prog.

def main(file):
    file = open(file,'r')
    word_list = file.read().split()
    real_word = []
    wordx = input('Please enter a jumbled word: ')
    word_l = wordx.lower()
    for word in word_list:
        if sorted(word) == sorted(word_l):
            real_word.append(word)
    if len(real_word) < 1:
        print('Your word cannot be unjumbled.')
    if len(real_word) == 1:
        print('Your word is %s.' %real_word[0])
    if len(real_word) > 1:
        print('Your words are: ')
        for i in range(len(real_word)):
            print(real_word[i])
    
main()
