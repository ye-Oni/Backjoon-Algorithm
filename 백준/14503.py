# 1. 아이디어
# while 문으로 계속 작동하도록 함 -> 특정 조건을 맞춘다면 종료!
# 4방향 for 문으로 탐색 먼저 수행 -> 빈칸이 있을 경우 이동
# 4방향 탐색이 안될 경우 -> 뒤로 한 칸 가서 반복
# 뒤로도 못간다면 -> while 문에서 빠져나오기

# 2. 시간복잡도
# O(NM) : 50^2 = 2500 < 2억
# While 문 최대 : N * M
# 각 칸에서 4방향 연산 수행 = N * M * 4(동서남북)

# 3. 자료구조
# 전체 지도 : int[][]
# 내 위치(y,x), 방향 : int, int, int
# 청소한 위치의 개수 : cnt


import sys
input = sys.stdin.readline

N,M = map(int, input().split())
y,x,d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]

while 1:
    if map[y][x] == 0:  # 청소가 안된 경우에만 청소를 하도록! 2-d에서 다시 돌아오는 경우를 대비
        map[y][x] = 2   # 현재 위치를 청소
        cnt += 1    # 다음 칸으로 이동
    sw = False
    for i in range(1,5):    # 동서남북
        ny = y + dy[d-i]    # 현재 방향을 기준으로 왼쪽 방향부터(뒤로가기 때문에 인덱스를 한 칸씩 줄여줘야 함.)
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M: 
            if map[ny][nx] == 0:    # 2-a.
                # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행
                d = (d-i+4) % 4
                y = ny  # 현재 위치가 탐색한 위치가 됨.
                x = nx
                sw = True   # break 이후 밑에 코드를 실행하지 않도록 하기 위해 변수 sw 선언 & True로 바꿔주기
                break   # for 문 종료 후 다시 1번부터 진행하게 됨(while)

    # 4방향 모두 있지 않은 경우
    if sw == False:
        # 뒤쪽 방향이 막혀있는지 확인
        ny = y - dy[d]  # 바라보고 있는 방향에서 한 칸 뒤로가기
        nx = x - dx[d]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx  # 여기서 끝내버리면 2번이 아닌 1번(while문 처음)으로 돌아가버림
        else:
            break

print(cnt)