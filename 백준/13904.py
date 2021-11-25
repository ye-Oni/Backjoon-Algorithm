n = int(input())

score = [list(map(int, input().split())) for _ in range(n)]
# 마감 기한과 과제 점수를 공백을 두고 n번만큼 입력받아서 리스트 형태로 score에 저장

score.sort(reverse=True, key=lambda x:x[1])
# 점수를 기준으로(인덱스 1번째 요소) 내림차순 정렬

result = [ 0 for _ in range(1001)]
# 최대 1000일의 과제 -> 반복문은 range 미만으로 계산되기 때문에 1001로 설정!
# 런타임 에러 주의

for d, w in score:
# score 안의 두 요소 마감기한(d), 점수(w)

    if result[d] == 0:  # 만약 result[d] 가 0 이라면 = 과제를 할 수 있는 날이라면
        result[d] = w   # 그 날에 점수 추가 (0이었던 값을 점수로 바꿔주기)

    else:   # 이미 다른 과제 점수가 들어있다면

        while d:    # d만큼 while문 반복 (d가 0이되면 false 이기 때문에 탈출)
            if w > result[d]:   # 만약 새로운 점수가 기존에 있던 점수보다 높다면
                result[d] = w  
                break   # 그 값으로 바꿔주고 반복문 탈출

            d -= 1  # 아니라면 d값을 1씩 감소시켜주기
            # 이 값을 감소시켜서 그 앞의 값들이랑 비교해서 현재 w가 result[d]보다 크다면
            # 다시 바꿔주기 -> 위 과정을 반복해서 최대한 마감기한이 많이 남은 것들부터 시작해서
            # 최대 점수를 넣어줄 수 있다!
            
print(sum(result))
# 최대 점수들이 모여있는 리스트인 result의 합을 출력해주기