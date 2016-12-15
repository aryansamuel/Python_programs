def main():
    principle = eval(input('Enter the intial amount of your investment: '))
    apr = eval(input('Please enter the apr: '))
    for i in range (10):
        principle = (1+apr)*principle
    print('Your principle is',principle)
    
main()
