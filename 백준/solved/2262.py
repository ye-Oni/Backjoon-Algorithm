n = int(input())

rank = list(map(int, input().split()))


hap = 0
for _ in range(len(rank)-1):

    target = max(rank)  # 가장 랭킹이 낮은 선수(숫자가 제일 큰 선수)
    idx = rank.index(target)    # 그 선수의 인덱스 위치

    if idx == 0:    # 맨 앞에 있는 선수가 랭킹이 제일 낮을 때
        hap += rank[idx] - rank[idx+1]
    elif idx == len(rank)-1:    # 맨 뒤에 있는 선수가 랭킹이 제일 낮을 때
        hap += rank[idx] - rank[idx-1]
    else:   # 양 쪽 선수들과 모두 비교를 해봐야 할 때
        hap += min(rank[idx]-rank[idx+1], rank[idx]-rank[idx-1])

    del rank[idx]   # 탈락한 선수는 리스트에서 제거해주기

print(hap)