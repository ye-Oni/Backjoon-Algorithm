m,n = map(int, input().split())

temp = []

for i in range(m):
    s = list(map(int, input().split()))
    pset = sorted(s)
    p_ind = []
    for j in s:
        p_ind.append(pset.index(j)+1)
    temp.append(p_ind)

count = 0

for i in range(len(temp)):
    for j in range(i+1 , len(temp)):
        if temp[i] == temp[j]:
            count += 1

print(count)


