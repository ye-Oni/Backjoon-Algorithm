n,m = map(int, input().split())

arr1 = []
arr2 = []

for _ in range(n):
    s = input()
    arr1.append(s)

for _ in range(m):
    test = input()
    arr2.append(test)

count = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i].startswith(arr2[j]) == True:
            count.append(arr2[j])

count = set(count)
count = list(count)

print(len(count))



# 다른 풀이 방법
n,m = map(int, input().split())

S = [input() for _ in range(n)]

print(S)

count = 0
for i in range(m):
    test = input()
    for j in S:
        if test == j[:len(test)]:
            count += 1
            break

print(count)









# from sys import stdin


# if __name__ == '__main__':
#     n, m = map(int, stdin.readline().split())
#     strings = {stdin.readline().strip() for _ in range(n)}
#     cnt = 0

#     for _ in range(m):
#         pattern = stdin.readline().strip()
#         for s in strings:
#             if s.startswith(pattern):
#                 cnt += 1
#                 break
#     print(cnt)