n = int(input())

arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[2])

print(*arr[0][:2])
print(*arr[1][:2])

if arr[0][0] == arr[1][0]:
    print(*arr[3][:2])
else:
    print(*arr[2][:2])

