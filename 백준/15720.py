b,c,d = map(int, input().split())

bp = sorted(list(map(int, input().split())), reverse=True)
cp = sorted(list(map(int, input().split())), reverse=True)
dp = sorted(list(map(int, input().split())), reverse=True)

total = sum(bp) + sum(cp) + sum(dp)

minValue = min(b,c,d)

cost = 0
for i in range(minValue):
    cost += (bp[0] + cp[0] + dp[0]) * 0.9
    bp.pop(0)
    cp.pop(0)
    dp.pop(0)

for i in range(len(bp)):
    cost += bp[i]

for i in range(len(cp)):
    cost += cp[i]

for i in range(len(dp)):
    cost += dp[i]

print(total)
print(int(cost))