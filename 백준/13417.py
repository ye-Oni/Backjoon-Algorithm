T = int(input())

for _ in range(T):
    N = int(input())
    init = list(input().split())

    arr = []
    arr.append(init[0])

    for i in range(1, len(init)):
        if init[i] <= arr[0]:
            arr.insert(0, init[i])
        else:
            arr.append(init[i])

    [ print(i, end='') for i in arr ]
    print()

