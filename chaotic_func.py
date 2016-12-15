def main():
    print('this program illustrates a chaotic function')
    j = eval(input('how many times do you want this response?: '))
    x = eval(input('enter a number between 0 and 1: '))
    for i in range(j):
           x = 3.9 * x * (1-x)
           print(x)

main()
           
