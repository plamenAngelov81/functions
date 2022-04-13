def orders(item, number):
    if item == "coffee":
        return number * 1.50
    elif item == "water":
        return number * 1.00
    elif item == "coke":
        return number * 1.40
    elif item == "snacks":
        return number * 2.00


product = input()
quantity = int(input())

print(f"{orders(product, quantity):.2f}")
