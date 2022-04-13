def add(a, b):
    return a + b


def subtract(d, c):
    return d - c


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = subtract(add(num1, num2), num3)

print(result)