def main():
    x = eval(input("Whats your weight(kg)? "))
    z = eval(input("And your height(m)? "))
    global a
    a = x/(z*z)
    if a<18.5:
        low()
    elif 18.5<=a<=24.9:
        b = "normal"
    elif 25<=a<=29.9:
        b = "high"
    else:
        b = "really high"

def low():
    print("%.2f is a" %a, "low BMI.")
    
main()
