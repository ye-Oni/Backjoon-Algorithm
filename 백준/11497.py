T = int(input())

for i in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    level = 0
    for j in range(n-2):
        level = max(level, abs(L[j]-L[j+2]))
    print(level)
