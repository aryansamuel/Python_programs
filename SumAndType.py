# Aryan Samuel
# arsamuel@ucsc.edu
# programming assignment 2
# the following program asks the user to enter a specific
#   number of grades, and then finds their average.

def main():
    x = eval(input('How many grades will you be entering?: '))
    if x%1 != 0:
        while True:
            x = eval(input("You can't enter %s grades! How many grades will you be entering? "%x))
            if x%1 == 0:
                break
    if x <= 0:
        while True:
            x = eval(input("You can't enter %s grades! How many grades will you be entering? "%x))
            if x > 0:
                break
    list = []
    for i in range(x):
        y = eval(input('Please enter a grade between 0 and 100: '))
        if 0 > y :
            while True:
                y = eval(input('Your number is out of range! Please enter a grade between 0 and 100: '))
                if 100 >= y >= 0:
                    break
        if y > 100:
            while True:
                y = eval(input('Your number is out of range! Please enter a grade between 0 and 100: '))
                if 0 <= y < 101:
                    break
        list.append(y)
    z = sum(list)/x
    if z > 69:
        print('Your class did great! The average was', z)
    if 70 > z > 59:
        print('Your class did okay. The average was', z)
    if z <= 59:
        print('Your class did poorly. The average was', z)
        
main()
