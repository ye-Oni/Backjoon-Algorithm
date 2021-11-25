N,K = map(int, input().split())

arr = []
for _ in range(N):
    A = int(input())
    arr.append(A)

arr.sort(reverse=True)

count = 0
for _ in range(len(arr)):
    if K > arr[0]:
        for i in arr:
            count += K // i
            K %= i
        break
    elif K < arr[0]:
        del arr[0]
        continue

print(count)