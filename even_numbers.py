def even_num(num_list):
    even_list = []
    for i in num_list:
        if int(i) % 2 == 0:
            even_list.append(int(i))

    return even_list


random_list = input().split(" ")

print(even_num(random_list))

# result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" ")))))
# print(result)
