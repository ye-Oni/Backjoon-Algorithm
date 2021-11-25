n = int(input())
P = [0 for i in range(n)]
sum = 0
min = 0
if (1<=n<=1000):
    P = list(map(int, input().split()))
    if len(P) == n:
        P = sorted(P)
        for i in range(n):
            sum += P[i]
            min += sum
        print(min)
