operator = input("Enter an operator (+, -, /, *, **): ")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "**":
    print(num1 ** num2)
else:
    print("Enter a valid operator!")
