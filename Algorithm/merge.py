#Merge Sort
# def merge(array):
#     if len(array) <= 1:
#         return array
    
#     mid = len(array) // 2
#     left = merge(array[:mid])
#     right = merge(array[mid:])
    
#     return merge_func(left, right)

# def merge_func(left, right):
#     merge_list = []
#     left_id, right_id = 0, 0
    
#     #case1 left, right
#     while len(left) > left_id and len(right) > right_id:
#         if left[left_id] > right[right_id]:
#             merge_list.append(right[right_id])
#             right_id += 1
#         else:
#             merge_list.append(left[left_id])
#             left_id += 1
    
#     #case2 letf
#     while len(left) > left_id and len(right) <= right_id:
#         merge_list.append(left[left_id])
#         left_id += 1
    
#     #case3 right
#     while len(right) > right_id and len(left) <= left_id:
#         merge_list.append(right[right_id])
#         right_id += 1
    
#     return merge_list
    

# #Test Code
# import random
# merge_array = random.sample(range(100), 10)

# print(merge_array)
# print(merge(merge_array))



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # divde 과정
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # list의 길이가 1이 될 때까지 divide
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    # 복사할 임시 배열
    copy = []

    # 양쪽 두 리스트 중 하나라도 원소가 없을 때까지 반복.
    while left and right:
        if left[0] < right[0]:
            copy.append(left.pop(0))
        else:
            copy.append(right.pop(0))

    # 만약 왼쪽 혹은 오른쪽 리스트가 남았을 때 모두 다 집어넣기
    if left:
        copy.extend(left)
    elif right:
        copy.extend(right)
    
    return copy

arr = [5, 2, 3, 9, 6, 1, 8, 4, 7]
print(merge_sort(arr))