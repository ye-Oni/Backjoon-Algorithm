n = int(input())

arr = []

for i in range(n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    arr.append([])
    arr[i].append(x)
    arr[i].append(y)
arr.sort(key=lambda x: (x[1], x[0]))

for i in range(len(arr)):   # 세로 크기
    for j in range(len(arr[i])):  # 가로 크기
        print(arr[i][j], end=' ')
    print()


# x,y의 좌표 값을 바꿔서도 할 수 있음!
