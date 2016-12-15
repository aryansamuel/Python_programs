def square_root():
    x = eval(input('insert a perfect square: '))
    for i in range(1,x,1):
        if x/i == i:
            print(i,'is the squareroot of',x,'.')

square_root()
