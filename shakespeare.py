# Aryan Samuel
# arsamuel@ucsc.edu
# programming assignment 4
# The following programn opens a text file, reads it, and then returns
# the number of times a word, entered by the user, is used in the text file.

def main(filex):
    filex = open(filex,'r')
    text = filex.read()
    y = ''
    import string
    for character in text:
        if character not in string.punctuation:
            y  = y + character
    x = (y.lower()).split()
    dictionary = {}
    for i in range(len(x)):
        word = x[i]
        dictionary[word] = x.count(word)
    return(dictionary)
   
main()
