def calculator(operator, a, b):
    if operator == "multiply":
        print(a * b)
    elif operator == "divide":
        print(f"{(a / b):.0f}")
    elif operator == "add":
        print(a + b)
    elif operator == "subtract":
        print(a - b)


operation = input()
num1 = int(input())
num2 = int(input())

calculator(operation, num1, num2)
