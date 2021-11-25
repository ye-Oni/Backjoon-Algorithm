T = int(input())

for _ in range(T):
    J,N = map(int, input().split())

    arr = []

    for _ in range(N):
        r,c = map(int, input().split())
        arr.append(r*c)

    arr.sort(reverse=True)

    for i in range(len(arr)):
        if J <= sum(arr[:i]):
            break   
    print(i)