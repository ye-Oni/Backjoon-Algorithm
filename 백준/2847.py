N = int(input())

arr = []
for _ in range(N):
    level = int(input())
    arr.append(level)

count = 0
for i in range(len(arr)-1, 0, -1):  # ex) arr의 길이는 3이지만 인덱스는 2까지 계산하기 때문에 -1을 해줌.
    for j in range(len(arr)-1, 0, -1):
        if arr[i] <= arr[j-1]:  # j는 i번째 요소보다 앞에 있는 수를 나타내야 하기 때문에(크기 비교) -1을 해줌.
            while True:
                if arr[i] <= arr[j-1]:  # arr[i] 값이 더 커질 때까지 반복!
                    arr[j-1] -= 1   # 1만큼 감소시키기
                    count += 1
                else:
                    break   # arr[i] > arr[j-1] 이면 반복문 탈출
    del arr[i]  # 한칸씩 앞으로 가서 비교하기 위해서 가장 큰 값은 삭제해주기!

print(count)

