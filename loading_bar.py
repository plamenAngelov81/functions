def load(num):

    percent = int(num / 10)
    points = int((100 - num) / 10)

    return f"[" + "%" * percent + "." * points + "]"


number = int(input())

if number == 100:
    print("100% Complete!")
    print(f"{load(number)}")
else:
    print(f"{number}% {load(number)}")
    print("Still loading...")
