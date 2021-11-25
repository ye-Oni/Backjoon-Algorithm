from random import randint

def selection_sort(arr):
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if arr[minIndex] > arr[j]:
                minIndex = j  # 최저값의 인덱스 저장
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        # 찾아낸 최솟값의 idx와 현재 idx에 있는 값을 swap한다.
    return arr

arr = [randint(1, 50) for i in range(8)]
n = len(arr)
print(selection_sort(arr))