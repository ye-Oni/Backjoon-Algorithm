# 재귀함수로 구현한 DFS

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, i, visited)


# Stack으로 구현한 DFS

# def dfs(graph, start, visited):
#     stack = [start, ]

#     while stack:
#         node = stack.pop()
#         print(node, end=' ')
#         stack.extend(graph[node])
#         if visited[node] == False:
#             visited[node] = True
            
        

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
dfs(graph, 1, visited)

# 1 2 7 6 8 3 4 5