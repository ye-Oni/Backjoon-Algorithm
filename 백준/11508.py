n = int(input())

arr = []

for _ in range(n):
    price = int(input())
    arr.append(price)
arr.sort(reverse=True)

n = 3
result = [arr[i*n:(i+1)*n] for i in range((len(arr)+n-1)//n)]

s = 0
for i in range(len(result)):
    s += sum(result[i][:2])

print(s)

