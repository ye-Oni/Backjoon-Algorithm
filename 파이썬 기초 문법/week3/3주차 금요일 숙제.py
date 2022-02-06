# p.263 연습문제
# # Q3
# print(all([1,2, abs(-3)-3]))    # False - 하나라도 거짓이면
# print(chr(ord('a')) == 'a')     # True - 아스키코드로 바꿨다가 다시 그 값을 문자로 바꿨기 때문에 원래 값과 동일함.

# # Q5
# print(int("0xea", 16))

# # Q8
# print(round(5.666666667, 4))

# # p.269 6-1
# while 문으로 풀기
# def GuGu(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n*i)
#         i += 1
#     return result

# print(GuGu(2))

## for문으로 풀기
# def GuGu(n):
#     result = []
#     for i in range(1,10):
#         result.append(i*n)
#     return result

# print(GuGu(2))


# 6-2
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)


# 6-3
def getTotalPage(a,b):
    if a % b == 0:
        return a // b
    return a // b + 1
print(getTotalPage(5, 10))
print(getTotalPage(30,10))
