import sys
input = sys.stdin.readline

n = int(input())
a = [input() for _ in range(n)]
ans = n*n
for k in range(1<<n):
    sum = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if k & (1<<j):
                if a[i][j] == 'H':
                    cnt += 1
            else:
                if a[i][j] == 'T':
                    cnt += 1
        sum += min(cnt, n-cnt)
    if ans > sum:
        ans = sum
print(ans)

# num = 24
# print(bin(num))	# 2진수

# print(oct(num))	# 8진수

# print(hex(num))	# 16진수

