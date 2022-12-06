number1 = float(input("Enter your first number:"))
op = input("Enter operator:")
number2 = float(input("Enter your second number:"))

if op == "+":
    print(number1 + number2)
elif op == "/":
    print(number1/number2)
elif op == "*":
    print(number1 * number2)
elif op == "-":
    print(number1-number2)
else:
    print("invalid operation")
