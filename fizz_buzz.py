def main():
    for i in range(1,1001):
        if i%3 == 0:
            print('fizz')
        elif i%5 == 0:
            print('buzz')
        elif i%5 == 0 and i%3 == 0:
            print('fizzbuzz')
        else:
            print(i)
            
main()
        