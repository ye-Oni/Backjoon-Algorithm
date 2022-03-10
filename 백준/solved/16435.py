n,s = map(int, input().split())
h = sorted(list(map(int, input().split())))


for i in range(n):
    if h[i] <= s:
        s += 1

print(s)

# for i in range(n):
#     s = s + length
#     length = 0
#     for j in range(len(h)):
#         if h[j] <= s:
#             length += 1
#     del h[0]

# print(s+length)
