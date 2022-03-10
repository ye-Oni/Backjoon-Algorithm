import sys 

arr1 = []
arr2 = []

for i in range(10):
    W = int(sys.stdin.readline())
    if (0<=W<=100):
        arr1.append(W)
arr1.sort(reverse=True)

for i in range(10):
    K = int(sys.stdin.readline())
    if (0<=K<=100):
        arr2.append(K)
arr2.sort(reverse=True)

print(arr1[0]+arr1[1]+arr1[2], end=' ')
print(arr2[0]+arr2[1]+arr2[2])