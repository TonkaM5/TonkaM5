from cal1 import added, multiply, subtract ,divided ,modular

def input_user():
    value1 = int(input("enter your first number:")) 
    operation = input("Enter the operation (+, -, *, /, %)")
    value2 = int(input("enter your second number:"))  
    return value1, operation, value2

value1, operation, value2 = input_user()
match operation: 
        case "+":
            print(f"{value1}+{value2} = {added(value1, value2)}")
        case "-":
            print(f"{value1}-{value2} = {subtract(value1, value2)}")
        case "*":
            print(f"{value1}*{value2} = {multiply(value1, value2)}")
        case "/":
            print(f"{value1}/{value2} = {divided(value1, value2)}")
        case "%":
            print(f"{value1}%{value2} = {modular(value1, value2)}")