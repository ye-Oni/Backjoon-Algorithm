from random import randint

def bubble_sort(arr):
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [randint(1,50) for i in range(8)]
n = len(arr)
print(bubble_sort(arr))