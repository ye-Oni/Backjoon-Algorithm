# # Q13
# import random
# result = []
# for i in range(6): 
#     num = random.randint(1,45)
#     if i not in result:
#         result.append(num)
# print(result)


# # p.269 6-1
# #while 문으로 풀기
# def GuGu(n):
#     result = []
#     i = 1
#     while i < 10:
#         result.append(n*i)
#         i += 1
#     return result

# print(GuGu(2))

# # for문으로 풀기
# def GuGu(n):
#     result = []
#     for i in range(1,10):
#         result.append(i*n)
#     return result

# print(GuGu(2))

# # 6-3
# def getTotalPage(a,b):
#     if a % b == 0:
#         return a // b
#     return a // b + 1
# print(getTotalPage(5, 10))
# print(getTotalPage(30,10))


# # 숙제 1
# A = [86, 44, 25, 63, 85, 100, 37, 96, 75]
# result = 0
# for i in A:
#     if i >= 50:
#         result += i
# print(result)

# # 숙제 2
# numbers = input("숫자 5개를 입력하세요 : ").split(",")
# result = 0
# for i in numbers:
#     result += int(i)
# print(result)
# print(result/len(numbers))

# # 리스트로 받아서 한번에 계산하기
# a = list(map(int, input("5개의 숫자를 입력하세요: ").split(',')))
# hap = sum(a)
# print(hap)
# print(hap/len(a))


# # 숙제 3
# num = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
# for i in range(1,10):
#     print(num * i)


# # 1
# print("Hello")