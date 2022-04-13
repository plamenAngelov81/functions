num = input()


def even_odd_sum():
    even_sum = 0
    odd_sum = 0
    for i in num:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


even_odd_sum()
