# for 문으로 각 숫자의 위치에서 이후 K개의 수를 더함
# 이 때마다 최댓값으로 갱신

# 1. 아이디어
# - 투포인터를 활용
# - for 문으로 처음에 K개 값을 저장
# - 다음 인덱스를 더해주고 , 이전 인덱스를 빼줌
# - 이 때마다 최댓값을 갱신

# 2. 시간복잡도
# - O(N) = 1e5 > 가능

# 3. 자료구조
# - 각 숫자들 N개 저장 배열 : int[]
#    - 숫자들 최대 100 > INT 가능
# K 개의 값을 저장 변수 : int
#   - 최대 : K * 100 = 1e5 * 100 = 1e7 > INT 가능
# - 최댓값 : int


import sys
input = sys.stdin.readline

N,K = map(int, input().split())
nums = list(map(int, input().split()))

each = 0

for i in range(K):  # K개를 더해주기
    each += nums[i]
    
maxv = each

# 다음 인덱스 더해주고 , 이전 인덱스 빼주기
for i in range(K, N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)