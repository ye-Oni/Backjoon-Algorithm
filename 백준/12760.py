# n,m = map(int, input().split())

# arr = []

# for _ in range(n):  # 카드 m개를 n명의 플레이어 수 만큼 입력 받기
#     cardNum = sorted(list(map(int, input().split())), reverse=True) # 내림차순 정렬
#     arr.append(cardNum) # 정렬한 cardNum을 arr에 추가

# final = []
# while True:
#     if len(arr[0]) == 0:  # while 루프를 빠져나가기 위해 arr[0]의 길이가 0이면 break
#         del[arr]
#         break

#     result = []
#     for i in range(len(arr)):
#         result.append(arr[i][0])    # arr[i][0]값들을 result에 추가(각 배열의 최댓값)
#         del arr[i][0]   # 한번 사용된 카드는 버리므로 삭제하기

#     maxNum = max(result)    # result에 저장된 값들 중 최댓값을 maxNum에 저장
#     j = 1   # 가장 큰 수를 가진 플레이어들이 여러명일 경우를 대비해서 비교하기
#     for j in range(1, len(result)+1):
#         if result[j-1] == maxNum:   # result의 j-1번째 요소부터 비교해서 maxNum과 같다면
#             final.append(j) # 그 값의 인덱스 j를 final에 저장하기

# count = {}  # 딕셔너리 count 선언
# for k in final: # 위의 과정에 걸쳐 점수를 획득한 플레이어들의 번호가 나열돼있는 final안에서
#     try: count[k] += 1  # 그 값이 있다면 1을 누적해서 더하고
#     except: count[k] = 1   # 없다면 1을 추가하기 (딕셔너리의 키와 값)
# # 각 플레이어의 번호가 총 몇 번이 나왔는지 세는 것 = 각 플레이어 별 획득한 점수의 합

# max_key = max(count.values())   # 딕셔너리 count의 밸류값들 중 최댓값을 찾아 max_key에 저장
# d = dict((key, value) for key, value in count.items() if value == max_key)
# # count에 저장돼있는 키와 밸류 값들 중 value가 위에서 구한 최댓값과 같다면
# [ print(k, end=' ') for k in d ]    # 그 인덱스 번호를 출력하기(가장 많은 점수를 획득한 플레이어들의 번호)




n,m = map(int, input().split())

arr = []
for _ in range(n):  # 카드 m개를 n명의 플레이어 수 만큼 입력 받기
    cardNum = sorted(list(map(int, input().split())), reverse=True)   # 내림차순 정렬
    arr.append(cardNum) # 정렬한 cardNum을 arr에 추가

card = n * [0]  # 플레이어 수 만큼 크기의 배열 생성(현재 값들은 0)
for i in range(m):
    maxNum = arr[0][i]   # arr[0][i] 번째 요소를 m에 저장
    for j in range(n):
        maxNum = max(maxNum, arr[j][i])   # m과 arr[j][i]번째 값을 계속 비교해서 최댓값을 m에 저장
    for j in range(n):
        if arr[j][i] == maxNum:  # 만약 arr[j][i]번째 값이 m과 같다면
            card[j] += 1    # 미리 선언해 둔 card의 j번째에 1을 누적해서 더하기

result = [] # 가장 많은 점수를 획득한 플레이어들이 여러명일 때 모두 출력하기 위한 과정
for i in range(len(card)):  # 각 플레이어들이 획득한 점수들이 모여있는 리스트 card
    if max(card) == card[i]:   # card의 최댓값이 card[i]번째 원소와 같으면 그 인덱스를 result에 저장 
        result.append(i+1) # 인덱스는 0부터 시작이므로 +1해서 저장
    
print(*result)  # result 리스트의 원소들을 출력





















