def rounding(string):
    new_list = []
    for i in string:
        new_i = round(float(i))
        new_list.append(new_i)
    return new_list


numbers = input().split(" ")

print(rounding(numbers))
