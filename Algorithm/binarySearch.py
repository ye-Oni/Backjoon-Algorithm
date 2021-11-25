def binary_search(data, target):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

my_list = [1, 9, 3, 5, 7, 13, 11, 17, 15]
my_list.sort()
print(binary_search(my_list, 5))