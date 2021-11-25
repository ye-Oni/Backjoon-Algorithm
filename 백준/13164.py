# N,K = map(int, input().split())
# h = list(map(int, input().split()))

# n = 2

# result = [h[i*n:(i+1)*n] for i in range((len(h)-1+n) // n )]

# cost = 0

# for i in range(len(result)):
#     if len(result[i]) == 2:
#         cost += result[i][1] - result[i][0]


# print(cost)


N,K = map(int, input().split())
h = list(map(int, input().split()))

arr = []

for i in range(N-1):
    a = h[i+1] - h[i]
    arr.append(a)

arr.sort()
cost = 0

for i in range(N-K):
    cost += arr[i]

print(cost)