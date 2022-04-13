def min_number(num_list):
    new_list = list(map(int, num_list))
    min_num = min(new_list)
    return min_num


def max_number(num_list):
    new_list = list(map(int, num_list))
    max_num = max(new_list)
    return max_num


def all_num_sum(num_list):
    new_list = list(map(int, num_list))

    total_sum = 0
    for i in new_list:
        total_sum += i
    return total_sum


numbers = input().split(" ")

print(f"The minimum number is {min_number(numbers)}")
print(f"The maximum number is {max_number(numbers)}")
print(f"The sum number is: {all_num_sum(numbers)}")

# second solution:

# def min_max_sum_fun(nums):
#    print(f"The minimum number is {min(nums)}")
#    print(f"The maximum number is {max(nums)}")
#    print(f"The sum number is: {sum(nums)}")


# numbers = list(map(int, input().split(" ")))
# min_max_sum_fun(numbers)
