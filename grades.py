def grades(num):
    if num <= 2.99:
        print("Fail")
    elif num <= 3.49:
        print("Poor")
    elif num <= 4.49:
        print("Good")
    elif num <= 5.49:
        print("Very Good")
    elif num <= 6.00:
        print("Excellent")


num1 = float(input())

grades(num1)
