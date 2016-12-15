def main():
    x = input('Please enter a properly encoded message: ')
    y = ''
    for character in x.split(','):
        character = int(character)
        y = y + chr(character)
    print(y)

main()
