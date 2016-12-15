def main():
    x = eval(input('choose your first number: '))
    y = eval(input('choose your second number: '))
    z = input('what would you like fizz to be? ')
    a = input('what would you like buzz to be? ')
    b = input('What would you like fizz buzz to be? ')
    c = eval(input('Till what number? '))
    for i in range(1,c+1):
        if i%x == 0:
            print(z)
        elif i%y == 0:
            print(a)
        elif i%x == 0 and i%y == 0:
            print(b)
        else:
            print(i)
            
main()
