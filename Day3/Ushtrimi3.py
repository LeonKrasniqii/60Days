number1 = float(input("Add a number you want to calculate: "))
operator = input("Enter operator (+,-,*,/):")
number2= float(input("Add second number you want to calculate: "))

if operator == "-":
    print(number1 - number2)
elif operator == "+":
    print(number1 + number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Invalid operation")