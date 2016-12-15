# Aryan Samuel
# arsamuel@ucsc.edu
# programming assignment 3
# The following program asks the user to enter a sentence,
# and the outputs the total number of words and the average word length.

def main():
    a = input('Please write a sentence. ')
    y = a.split()
    list = []
    z = ''
    import string
    for character in y:
        if character not in string.punctuation:
            list.append(character)
    print('Your sentence has',len(list),'words.')
    for character in a:
        if character not in string.punctuation:
            z = z + character
    z = z.replace(' ', '')
    avg_z = len(z)/len(list)
    print('The average word length of your sentence is approximately %.2f.' %avg_z)

main()
