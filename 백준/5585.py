N = int(input())

money = [500, 100, 50, 10, 5, 1]

m = 1000 - N
count = 0
for i in money:
    count += m // i
    m %= i

print(count)