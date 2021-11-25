fib = [1, 2]    # 서로 다른 수를 써야하므로 1부터 저장 (0,1 제외)
# 풀이 (2)번 참고
for i in range(2, 43):  # 44번째까지 사용할 수 있으므로 -2해서 42번째 요소까지 사용가능!
    fib.append(fib[i-1] + fib[i-2])

fib.sort(reverse=True)  # 풀이 (3)번 참고
#print(fib)

T = int(input())

for j in range(T):
    n = int(input())
    result = []

    for k in fib:   # 풀이 (5)번 참고
        if k <= n:
            result.append(k)
            n -= k
            
        result.sort()

    print(*result)


 