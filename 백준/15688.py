import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    number = int(sys.stdin.readline())
    arr.append(number)
    
arr.sort()

[print(i) for i in arr]

