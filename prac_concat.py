def main():
    x = input('Please enter your first name: ')
    y = input('Please enter your last name: ')
    a = eval(input('Please enter the number of the month you were born: '))
    list = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
    z = x[0]+y[0:7]
    lowerx = z.lower()
    print(lowerx+list[a-1])
main()
