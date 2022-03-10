N = int(input())    # 동전의 수
first = list(map(int, input().split()))   # 1라운드 동전들
second = list(map(int, input().split()))  # 2라운드 동전들

sum = 0
for i in first:
    sum += abs(i)

for j in second:
    sum += abs(j)

print(sum)