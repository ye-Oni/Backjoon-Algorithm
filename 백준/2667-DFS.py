# 백준 2667번 DFS로 풀기

#  이중 for문 사용 => 1이고, False이면 그래프 탐색 시작
#  재귀함수 호출(DFS) - 연결돼있는 걸 계속 파고들기
#  위 값을 리스트에 저장 & 정렬한 후 출력하기

# 1. 아이디어
# - 2중 for문, 값 1 && 방문 X => DFS
# - DFS를 통해 찾은 값을 저장 후 정렬해서 출력하기

# 2. 시간복잡도
# - DFS : O(V+E)
# - V, E : N^2, 4N^2
# - V+E = 5N^2 ~= N2 ~= 625 >> 가능함

# 3. 자료구조
# - 그래프 저장 : int[][]
# - 방문여부 : bool[][]
# - 결과값 : int[]




import sys
from typing import FrozenSet
input = sys.stdin.readline  # 엔터 친 것이 특수문자로 들어옴 -> strip함수 사용

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []

each = 0    # 각 단지 내 집의 수

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    global each # 전역 변수 사용
    each += 1   # 크기 측정
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx) # 재귀 호출


for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            chk[j][i] = True
            # DFS로 크기 구하기
            each = 0    # 새로운 노드를 방문할 때마다 크기를 초기화해주기
            dfs(j,i)
            # 크기를 결과 리스트에 넣기
            result.append(each)

result.sort()   # 오름차순 정렬

print(len(result))  # 총 단지수
for i in result:
    print(i)    # 한 줄에 하나씩 출력





