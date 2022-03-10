N, K = input().split()
N = int(N)
K = int(K)
arr = list(map(int,input().split()))

sub = 0
for i in range(K):
    sub += i

arr.sort(reverse=True)
result = 0
for i in range(K):
    result += arr[i]

answer = result - sub
print(answer)



