def factorial(num):
    result = num
    if num == 0:
        result = 1
    else:
        for num in range(num - 1, 0, -1):
            result = result * num

    return result


num1 = int(input())
num2 = int(input())

division = factorial(num1) / factorial(num2)

print(f"{division:.2f}")
