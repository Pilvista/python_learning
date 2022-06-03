num1 = float(input("Enter your first digit: "))
operator = input("Enter your operator: ")
num2 = float(input("Enter your second digit: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")


