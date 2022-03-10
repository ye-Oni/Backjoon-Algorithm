# n = int(input())

# a = sorted(list(map(int, input().split())))

# result = 0

# for i in range(len(a)-1):
#     cost = (sum(a) - a[0]) * a[0]
#     result += cost
#     del a[0]

# print(result)


n = int(input())

a = list(map(int, input().split()))

result = 0
sumOfList = sum(a)

for i in range(len(a)-1):
    sumOfList -= a[i]
    result += a[i] * sumOfList

print(result)



# n = int(input())
# A = list(map(int, input().split()))
# res = 0
# Len = sum(A)
# for i in range(len(A)-1):
#     Len -= A[i]
#     res += A[i] * Len
# print(res)

