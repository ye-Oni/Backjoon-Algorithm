n = int(input())

for i in range(n):
    a,b = input().split()
    A = sorted(a)
    B = sorted(b)
    if A == B:
        print(str(a)+' &', b, 'are anagrams.')
    else:
        print(str(a)+' &', b, 'are NOT anagrams.')
