num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
else:
    if operator == "-":
        print("Result:", num1 - num2)
    else:
        if operator == "*":
            print("Result:", num1 * num2)
        else:
            if operator == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Division by zero is not allowed")
            else:
                print("Invalid operator")