N = int(input())    # 손님에게 거슬러주어야 할 돈 N원 입력받기

coin = [500, 10, 50, 100]   # 500원,100원,50원,10원 동전이 무한히 존재
coin.sort(reverse=True) # 값이 가장 큰 동전부터 써서 거슬러주어야 최소 횟수를 구할 수 있으므로 내림차순 정렬

count = 0   # 거슬러주어야 할 동전의 개수(최소 횟수)를 카운트하기 위해 선언
for i in coin:  
    count += N // i # N원을 리스트 coin의 i번째 요소로 나눈 몫(=거슬러줄 때 필요한 동전의 개수)을 count에 누적해서 저장
    N %= i  # N원을 i번째 요소로 나눈 나머지를 다시 N에 저장
    # 이미 위에서 거슬러준 후 남은 값을 가지고 다시 위의 과정 반복
print(count)