# N,K = map(int, input().split())

# arr = []
# for _ in range(N):
#     A = int(input())
#     arr.append(A)

# arr.sort(reverse=True)

# count = 0
# for _ in range(len(arr)):
#     if K > arr[0]:
#         for i in arr:
#             count += K // i
#             K %= i
#         break
#     elif K < arr[0]:
#         del arr[0]
#         continue

# print(count)



# 두 번째로 풀었을 때
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.reverse()

cnt = 0

for i in range(N):
    cnt += K // A[i]
    K %= A[i]
    
print(cnt)
    