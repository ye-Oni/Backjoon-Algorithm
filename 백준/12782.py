# T = int(input())


# for _ in range(T):
#     result = 0
#     n,m = input().split()
#     n = list(n)
#     m = list(m)
#     if n != m:
#         result += 1
#         if n.count('1') != m.count('1'):
#             result += abs(n.count('1') - m.count('1'))

#     print(result)


T = int(input())

for _ in range(T):
    n,m = map(str, input().split())
    one = 0
    zero = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            if m[i] == '1':
                one += 1
            else:
                zero += 1
    print(max(one, zero))


