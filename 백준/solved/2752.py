a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
arr = []
arr.append(a)
arr.append(b)
arr.append(c)
arr = sorted(arr)
for i in arr:
    print(i, end=" ")
    
# 간결하게
num = list(map(int, input().split()))
num.sort()
print(num[0],num[1],num[2])