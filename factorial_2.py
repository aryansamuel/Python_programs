def main():
    x = eval(input('Find factorial of which number: '))
    for i in range(1, x):
        x = x*i
    print(x)
main()
