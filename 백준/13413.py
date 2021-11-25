T = int(input())

for _ in range(T):
    N = int(input())
    init = list(input())    # 초기상태(리스트로 저장)
    final = list(input())   # 목표상태
    
    cnt = 0
    cnt2 = 0

    if init.count('B') == final.count('B'): # init와 final의 검정색,흰색말의 개수가 같을 때
        for i in range(N):
            if init[i] != final[i]: # 만약 두 리스트의 i번째 값이 다르다면 바꿔야 하므로
                cnt += 1    # 바꾸는 횟수를 의미하는 변수 cnt에 1 더하기

        print(int(cnt/2))   # 두 요소를 바꾸는 횟수 2번 = 실제로 1번 바꿈 (나누기 2 해주기)

    else:   # init와 final의 검정색,흰색말의 개수가 다를 때
        for i in range(N):

            if init.count('B') != final.count('B'): # 다르다면
                if init[i] != final[i]: # 위와 달리 조건 2 먼저 사용!
                    final[i] = init[i]  # 두 값이 다르다면 final의 i번째 요소를 init의 i번째 요소 값으로 바꿔주기
                    cnt += 1  # 바꿨으니까 cnt에 1 더하기

            else:   # 위의 if문을 반복하다보면 검정색,흰색 말의 개수가 같아지는 순간이 옴.
                if init[i] != final[i]: # 조건 1 사용
                    cnt2 += 1   # 위에서 쓴 변수랑 겹치지 않게 cnt2에 1 더하기

        print(cnt + int(cnt2/2))    # 조건2를 통해 계산된 cnt와 조건 1을 사용해 계산된 (cnt2/2)를 더한 값 출력
                                    # 그게 최종 바꾼 횟수!!!








# T = int(input())

# for _ in range(T):
#     N = int(input())    # 입력받을 말의 개수(길이)
#     init = list(input())    # 초기상태
#     final = list(input())   # 목표상태

#     black = 0
#     white = 0

#     for i in range(N):
#         if init[i] != final[i]: # 초기상태의 i번째 요소와 목표상태의 i번째 요소가 다를 때
#             if final[i] == 'W': # 그 값이 W라면
#                 white += 1  # white 변수에 1 누적해서 더하기
#             else:   # 그 값이 B라면
#                 black += 1  # black 변수에 1 누적해서 더하기
    
#     print(max(white, black))    # 계산된 두 값 black,white중 더 큰 값을 출력









T = int(input())
for _ in range(T):
    N = int(input())
    init = list(input())
    final = list(input())

    cnt = 0
    cnt2 = 0

    for i in range(N):
        if init[i] != final[i]:
            if init[i] == 'W':
                cnt += 1
            else:
                cnt2 += 1

    print(cnt + cnt2 -min(cnt, cnt2))