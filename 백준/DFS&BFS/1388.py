"""문제의 조건"""
# 나무 판자의 크기 = 1, 양수의 길이
# 기훈이 방은 직사각형, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어짐
# '-'와 'ㅣ'로 이루어진 바닥 장식 모양
# 두 개의 '-'가 인접해있고 같은행, 두 개의 'ㅣ'가 인접해있고 같은 열이면 같은 나무 판자

"기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수는?"


"""# dfs 알고리즘 사용하기"""
def dfs(x,y):
    # 바닥 장식 모양이 '-' 일 때
    if graph[x][y] == '-':
        # 해당 노드 방문처리
        graph[x][y] = 1
        for _y in [1,-1]:   # 양옆(좌우) 확인하기
            Y = y + _y
            # 좌우 노드가 주어진 범위를 벗어나지 않고 '-'모양이라면 재귀함수 호출
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x,Y)
    # 바닥 장식 모양이 '|' 일 때
    if graph[x][y] == '|':
        # 해당 노드 방문처리
        graph[x][y] = 1
        for _x in [1,-1]:
            X = x + _x  # 상하(위아래) 확인하기
            # 상하 노드가 주어진 범위를 벗어나지 않고 '|' 모양이라면 재귀함수 호출
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X,y)

n,m = map(int, input().split()) # 방 바닥의 세로 크기 n, 가로 크기 m
graph = []  # 2차원 리스트의 맵 정보 저장할 공간
for _ in range(n):
    graph.append(list(input()))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i,j)    # 노드가 '-'이나 '|'일 경우에 재귀함수 호출
            count += 1

print(count)


"""알고리즘 없이 풀기"""
# # '-'모양의 나무 판자 개수 계산
# count = 0
# for i in range(n):
#     a = ''
#     for j in range(m):
#         if graph[i][j] == '-':
#             if graph[i][j] != a:
#                 count += 1
#         a = graph[i][j]
#
# # 'ㅣ'모양의 나무 판자 개수 계산
# for j in range(m):
#     a = ''
#     for i in range(n):
#         if graph[i][j] == '|':
#             if graph[i][j] != a:
#                 count += 1
#         a = graph[i][j]
#
# print(count)

