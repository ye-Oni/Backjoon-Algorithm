arr = []
arr2 = []
arr3 = []
sum = 0

for i in range(8):
    s = int(input())
    if (0<=s<=150):
        arr.append(s)

for i, score in enumerate(arr):
    arr2.append([])
    arr2[i].append(score)
    arr2[i].append(i+1)

arr2 = sorted(arr2, reverse=True)

for i in range(5):
    sum += arr2[i][0]
    a = arr2[i][1]
    arr3.append(a)

arr3 = sorted(arr3)

print(sum)

for i in arr3:
    print(i, end=' ')




