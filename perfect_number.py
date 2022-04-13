def perf_num(num):
    list_num = []
    for i in range(1, num):
        if num % i == 0:
            list_num.append(i)
    return list_num


number = int(input())

if sum(perf_num(number)) == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")