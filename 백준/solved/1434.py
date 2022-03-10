n,m = map(int, input().split()) # 박스의 개수 n, 책의 개수 m

A = list(map(int, input().split()))   # 박스의 용량
B = list(map(int, input().split()))   # 책의 크기

print(sum(A)-sum(B))





# # B가 리스트형일 때

# A = ['one2ye', 'loves', '20s']
# B = ['me', 'too']

# A.append(B)
# print(A)

# A = ['one2ye', 'loves', '20s']
# B = ['me', 'too']

# A.extend(B)
# print(A)



# # B가 문자열일 때

# A = ['one2ye', 'loves', '20s']
# B = 'happy'

# A.append(B)
# print(A)

# A = ['one2ye', 'loves', '20s']
# B = 'happy'

# A.extend(B)
# print(A)