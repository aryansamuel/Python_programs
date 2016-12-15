def main():
    x = input('What message would you like to make a secret? ')
    y = ''
    for character in x:
        y = y + str(ord(character)) + ',' + ' '
    print('The encoded message is:', y)

main()
