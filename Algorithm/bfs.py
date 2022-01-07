from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용 - 젤 처음에는 큐에 1만 들어가있음
    queue = deque([start]) 
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력 - 제일 왼쪽 끝 요소를 가져오면서 삭제하기
        v = queue.popleft()
        print(v, end=' ')   # 먼저 방문하는 순서(실행 결과) 출력
        # 해당 원소 v와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 - ex) 
        for i in graph[v]:
            if not visited[i]:  # 만약 visitied[i] 요소가 False라면
                queue.append(i) # 추가하고
                visited[i] = True   # True로 바꿔주기

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],       # 처음 v가 1이기 때문에 빈 리스트 하나 넣어줌
  [2, 3, 8], 
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트) - 0부터 시작하기 때문에 9개 곱하기
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)


