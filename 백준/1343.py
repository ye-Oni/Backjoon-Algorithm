N = input()

N = N.replace("XXXX", "AAAA")
N = N.replace("XX", "BB")

if N.count('X') >= 1:
    print('-1')
else:
    print(N)

