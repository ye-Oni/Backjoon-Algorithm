# N = int(input())

# arr = []
# for _ in range(N):
#     word = list(input())
#     arr.append(word)

# count = 0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] != arr[j] and sorted(arr[i]) == sorted(arr[j]):
#             count += 1
#         elif len(arr[i]) == 1 and arr[i] == arr[j]:
#             count += 1
# print(count)


n = int(input())

arr = []
for _ in range(n):
    word = sorted(list(input()))
    word = ''.join(word)
    if word not in arr:
        arr.append(word)

print(len(arr))








