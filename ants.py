# Aryan Samuel
# arsamuel@ucsc.edu
# programming assignment 5
# The following program prints the lyrics for the song, "The ants go marching".

def hurrah():
    list_numb = ['one','two','three','four','five','six','seven','eight','nine','ten']
    list_words = ['suck his thumb,','tie his shoe,','climb a tree,','shut the door,','take a dive,','pick up sticks,','look up to heaven,','shut the gate,','check the time,','say the end,']
    for i in range(10):
        print('The ants go marching ' +list_numb[i]+ ' by ' +list_numb[i]+ ', hurrah! Hurrah!')
        print('The ants go marching ' +list_numb[i]+ ' by ' +list_numb[i]+ ', hurrah! Hurrah!')
        print('The ants go marching ' +list_numb[i]+ ' by ' +list_numb[i]+ ',')
        print('The little one stops to', list_words[i])
        boom()

def boom():
    print('And they all go marching down...')
    print('In the ground...')
    print('To get out...')
    print('Of the rain.')
    print('Boom! Boom! Boom!')

hurrah()
