# 백준 1926번 문제 - BFS로 풀기

# 1. 아이디어
# - 2중 for => 값 1 && 방문 X => BFS
# - BFS 돌면서 그림 개수 +1, 최댓값을 갱신

# 2. 시간복잡도
# - BFS : O(V+E) = V + 4V = 5V = 5(m*n) 
# - V : m * n = 500 * 500 (m, n이 최대 500 이므로)
# - E : V * 4
# - V+E : 5 *250000 = 100만 < 2억 이므로 가능함!

# 3. 자료구조
# - 그래프 전체 지도 : int[][]
# - 방문 : bool[][]
# - Queue(BFS)


from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]   # 그래프 전체 지도
chk = [[False] * m for _ in range(n)]   # 방문 check

dy = [0,1,0,-1] # 오른쪽, 밑, 왼쪽, 위 방향
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1  # (y,x) 한 개가 이미 존재하기 때문
    q = deque()
    q.append((y, x))    # 시작 노드를 큐에 넣어줌
    while q:
        ey, ex = q.popleft()
        for k in range(4):  # 최대 4개의 방향(동서남북)으로 확인해볼 수 있기 때문에 4번 반복
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1 # 그림의 크기 늘리기
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0     # 전체 그림 갯수
maxv = 0    # 최대 크기

for j in range(n):   # 보통 2중 for문에서는 y(세로)를 먼저 도는 식으로 함.
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:    # 값이 1인데 방문하지 않은 BFS를 판별하기
            chk[j][i] = True
            # 전체 그림 갯수 +1
            cnt += 1
            # BFS -> 그림 크기를 구해주고 최댓값 갱신해주기
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)
