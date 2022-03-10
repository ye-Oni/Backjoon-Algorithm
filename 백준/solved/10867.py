n = int(input())
L = list(map(int, input().split()))
if n == len(L) and (1<=n<=100,000):
    L = sorted(set(L))
    for i in L:
        print(i, end=' ')