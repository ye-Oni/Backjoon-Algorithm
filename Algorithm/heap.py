# def heap_sort(a):
#     for i in range(1,len(a)): # 최대 힙 만들기
#         c = i
#         while c != 0:
#             r = (c-1) // 2
#             if a[r] < a[c]:
#                 a[r], a[c] = a[c], a[r]

#             c = r

#     for j in range(len(a)-1,-1,-1): # 힙 만들기
#         a[0], a[j] = a[j], a[0]
#         r = 0
#         c = 1

#         while c < j:
#             c= 2 * r + 1
#             if c < j -1 and a[c] < a[c+1]:
#                 c += 1

#             if c < j and a[r] < a[c]:
#                 a[r], a[c]=a[c], a[r]

#             r = c 

# b = [5, 2, 3, 9, 6, 1, 8, 4, 7]
# heap_sort(b)

# # 결과>>[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(b)


def heapify(arr, index, heap_size):
    largest = index
    left = index * 2 + 1 # 왼쪽 자노드
    right = index * 2 + 2 # 오른쪽 자노드
    # 왼쪽 자식이 현재 요소보다 크면 인덱스 교체!
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    # 오른쪽 자식이 현재 요소보다 크면 인덱스 교체!
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    # 교체된 적이 있다면 교체된 index와 largest 요소값 교체!
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        # 변경된 부분을 중심으로 다시 한번 heapify
        heapify(arr, largest, heap_size)

def heap_sort(arr):
    n = len(arr)

    # 최초 힙
    # 트리의 절반부터 거꾸로 올라가며 하는 것이 효율적
    for i in range(n // 2 -1, -1, -1):
        heapify(arr, i, n)
    # 한번 구성된 힙을 정렬
    # 가장 큰 값(루트) 을 가장 끝 값으로 이동한 후 힙 생성.
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

arr = [5, 2, 3, 9, 6, 1, 8, 4, 7]
print(heap_sort(arr))