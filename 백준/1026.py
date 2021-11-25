# 길이가 N인 정수 배열 A와 B
# 함수 S = A[0]*B[0]+...+A[N-1]*B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열 하자!! (B는 안됨)
# S의 최솟값은?

n = int(input())

arr = []
sum = 0

A = [0 for i in range(n)]
B = [0 for i in range(n)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if (len(A) == n) and (len(B) == n):

    for i in range(n):
        arr.append(max(A)*min(B))
        A.remove(max(A))
        B.remove(min(B))
        
    for i in arr:
        sum += i
    print(sum)