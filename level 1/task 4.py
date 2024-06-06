#level1-T4
#Task: Calculator Program
#Create a Python program that acts as a basic calculator. It should prompt the user toenter two numbers and an operator (+, -,*, /,%), and then display the result of the operation.
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator to be performed(+, -, *, /): ")
    
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operator.")

calculator()
