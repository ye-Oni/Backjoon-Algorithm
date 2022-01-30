# # 숙제 1
# a = [1,2,3,3,3,4,5]
# count = 0
# for i in a:
#     if i == 3:
#         count += 1
# print(count)


#  # 숙제 2
# num = int(input("1부터 10까지의 정수 중 하나를 입력해주세요: "))
# for i in range(1,num+1):
#     print(i)

# a = int(input())
# for i in range(a):
#     a = a+i
# print(a)


# # 숙제 3
# score = int(input("점수를 입력하세요: "))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")
 
 
#  # 숙제 4
# def jiyoon(a,b,c,d):
#     result = a + b + c + d
#     return result
# print(jiyoon(1,2,3,4))





    
# p.146
# # 연습문제 2
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         result += i
#     i += 1
# print(result)


# # 연습문제 3
# i = 0
# while True:
#     i += 1
#     if i > 5:
#         break
#     print(i*'*')


# # 연습문제 4
# for i in range(1,101):
#     print(i)


# # 연습문제 5
# A = [70, 60, 55, 75, 95, 90, 80, 80 , 85, 100]
# total = 0
# for score in A:
#     total += score
# average = total / len(A)
# print(average)


# # 연습문제 6
# numbers = [1,2,3,4,5]
# result = [n*2 for n in numbers if n % 2 == 1]
# print(result)


# # p.179 연습문제 1
# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# print(is_odd(3))





# # 연습문제 3
# input1 = int(input("첫번째 숫자를 입력하세요: "))
# input2 = int(input("두번째 숫자를 입력하세요: "))

# total = input1 + input2
# print("두 수의 합은 %s 입니다" %total)


# 연습문제 4
# 3번 : 쉼표는 띄어쓰기 역할을 한다.








# # 코딩면허시험 4번
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# result = 0
# for i in A:
#     if i >= 50:
#         result += i
# print(result)


# # 코딩면허시험 5번
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-2) + fib(n-1)

# n = int(input())

# for i in range(n):
#     print(fib(i))


# # 코딩면허시험 6번
# n = input()
# n2 = n.split(',')
# total = 0
# for i in n2:
#     total += int(i)

# print(total)


# # 코딩면허시험 7번
# n = int(input("2~9까지의 숫자들 중 하나를 입력하세요: "))
# for i in range(1,10):
#     print(i*n, end=' ')
    