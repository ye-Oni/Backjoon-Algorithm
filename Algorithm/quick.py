# from random import randint
 
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left_arr, mid_arr, right_arr = [], [], []
#     for i in arr:
#         if i < pivot:
#             left_arr.append(i)
#         elif i > pivot:
#             right_arr.append(i)
#         else:
#             mid_arr.append(i)
#     return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)
 
# arr = [randint(1,50) for i in range(8)]
# print(quick_sort(arr))

from random import randint

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, mid, right = [], [], []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            mid.append(i)
    return quick_sort(left) + mid + quick_sort(right)

arr = [randint(1, 50) for i in range(8)]
print(quick_sort(arr))