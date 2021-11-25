n = int(input())
alist = []
for i in range(n):
    arr = list(map(int, input().split()))
    arr = sorted(arr, reverse=True)
    alist.append(arr)

[print(alist[i][2]) for i in range(n)]

