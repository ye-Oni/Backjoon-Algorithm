T = int(input())    # Test Case

alist = []

for _ in range(T):
    arr = []
    N = int(input())

    for _ in range(N):
        S,L = input().split()
        L = int(L)
        arr.append([L, S])
        arr.sort(reverse=True)
    alist.append(arr)

[print(alist[i][0][1]) for i in range(len(alist))]


# T = int(input())    # Test Case
# for _ in range(T):
#     N = int(input())
#     arr = []
#     for i in range(N):
#         S,L = input().split()
#         L = int(L)
#         arr.append([S, L])
#         arr = sorted(arr, key = lambda x: x[1])
# print(arr[-1][0])

