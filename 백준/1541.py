N = input().split('-')

s = 0
for i in N[0].split('+'):
    s += int(i)
for i in N[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)
    
