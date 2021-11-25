N = int(input())    # 팬의 수

time = [list(map(int, input().split())) for _ in range(N)]  # N개의 줄에 걸쳐 s,e 입력받기

s = sorted(time, reverse=True)    # s값을 기준으로 정렬
e = sorted(time, key=lambda x:x[1]) # e값을 기준으로 정렬

# 가장 늦게 등교한 학생 - 가장 빨리 하교한 학생
if (s[0][0]-e[0][1]) < 0:   
    print(0)    # 0보다 작다는건 욱제가 학교에 머물러야 할 시간이 없다는 뜻!
else:
    print(s[0][0]-e[0][1])