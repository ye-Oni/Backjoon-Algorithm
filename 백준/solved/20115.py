N = int(input())    # 에너지 드링크 수

x = sorted(list(map(int, input().split())), reverse=True)
# 에너지 드링크의 양

amount = x[0]
for _ in range(len(x)-1):
    amount += x[1]/2
    del x[1]

print(amount)