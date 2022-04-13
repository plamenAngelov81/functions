def sort(num_list):
    new_list = list(map(int, num_list))
    new_list.sort()
    print(new_list)


numbers = input().split(" ")

sort(numbers)
