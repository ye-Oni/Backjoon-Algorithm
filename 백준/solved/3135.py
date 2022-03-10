A, B = map(int, input().split())
N = int(input())

arr = []
[arr.append(int(input())) for _ in range(N)]

min_value = 1001
idx = 0
for i in arr:
    temp = abs(i - B)
    if min_value > temp:
        min_value = temp
        idx = i

print(min(abs(A-B), (abs(idx-B)+1)))

