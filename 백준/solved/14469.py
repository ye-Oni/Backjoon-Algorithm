# n = int(input())

# arr = []

# for _ in range(n):
#     a,b = map(int, input().split())
#     arr.append([a,b])

# arr.sort()

# time = 0

# for i in range(len(arr)-1):
#     time = arr[i][0] + arr[i][1]
#     if time > arr[i+1][0]:
#         time = time + arr[i+1][1]

# print(time)

n = int(input())

arr = []

for _ in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])

arr.sort()

time = 0

for i in range(len(arr)):
    if time > arr[i][0]:
        time = time + arr[i][1]
    else:
        time = arr[i][0] + arr[i][1]

print(time)