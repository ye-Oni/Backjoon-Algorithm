S = str(input())
n = len(S)
arr = []

for i in range(n):
    arr.append(S[i:])
arr = sorted(arr)

for i in arr:
    print(i)
