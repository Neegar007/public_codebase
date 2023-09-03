# This script accepts two numbers and perform calculations on them

def calc(num1, opp, num2) :
    
    operation = ["+", "-", "/", "*"]
    num1Val = type(num1)
    num2Val = type(num2)
    
    print(num1Val)
    if num1 is int :
        print("Only numbers are allowed")
    else :
        for op in operation :
            if op == opp :
                print(eval(f"{num1} {opp} {num2}"))
    
    
dig1 = 25
opp = "+"
dig2 = 425

calc(dig1, opp, dig2)