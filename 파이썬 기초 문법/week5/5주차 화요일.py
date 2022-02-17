# # 42
# a = float(input())
# print(round(a, 2))    # 1개만 입력받았기 때문에 round 함수를 사용해도 무방

# # 43
# f1,f2 = input().split()
# result = float(f1)/float(f2)
# # print(round(result, 3))
# print('%.3f'%result)    # round 함수만 사용하면 10.0/0.0001 일때 애초에 소수자리가 하나밖에 안나와서 예외가 발생함
# print(format(result,".3f"))

# # 44
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(round(a/b,2)) # a,b가 정수이기 때문에 예외발생가능성 X, round 함수 사용가능

# # 45
# a,b,c = input().split()
# hap = int(a) + int(b) + int(c)
# avg = hap / 3
# print(hap,format(avg,".2f"))    # format 함수를 사용해서 소수점 둘째자리까지 출력
# print(hap,("%.2f"%avg))

# # 46
# a = int(input())
# #비트연산자 풀이
# print(a<<1)
# print(a*2)

# # 47
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a*(2**b))
# #비트연산자 풀이
# print(a<<b)

# # 48
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a<b)

# # 49
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a==b)

# # 50
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(b>=a)

# # # 51
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a!=b)

# 52
# n = int(input())
# print(bool(n))

# # 53
# n = bool(int(input()))  # input으로 입력받고 int로 정수변환하고 bool로 1과0으로만(true/false) 표현되게 변환한 변수 n
# print(not n)    # bool을 안써도 값이 출력되긴 함.

# # 54
# a,b = input().split()   # bool을 앞에 써주지 않으면 1과 0으로 값이 반환됨.
# print(bool(int(a)) and bool(int(b)))    # 둘 다 참이어야 True 반환(즉, 하나라도 0이 있으면 안됨)

# # 55
# a,b = input().split()   # bool을 앞에 써주지 않으면 1과 0으로 값이 반환됨.
# print(bool(int(a)) or bool(int(b)))    # 하나라도 참이면 True 반환(즉, 둘다 0일때만 false)

# # 56
# a,b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# print((a and (not b)) or (not a) and b) # XOR(배타적 논리합: 참,거짓이 서로 다를 때만 True로 계산 => 공식이므로 외우기)

# # 57
# a,b = input().split()
# print(bool(int(a) == bool(int(b))))

# # 58
# a,b = input().split()
# print(bool(int(a))==False and bool(int(b))==False)
# print( not (c or d) )

# # 59
# a = int(input())
# print(~a)

# # 60
# a,b = input().split()
# print(int(a) & int(b))

# # 61
# a,b = input().split()
# print(int(a) | int(b))

# # 62
# a,b = input().split()
# print(int(a) ^ int(b))

# 63
# a,b = input().split()
# a = int(a)
# b = int(b)
# c = (a if (a>=b) else b)    # 괄호 안의 (a>=b)의 값이 참이면 a출력 거짓이면 b출력
# print(c)
# # 삼항연산자 사용없이 풀기
# a,b = input().split()
# a = int(a)
# b = int(b)
# if a > b:
#     print(a)
# else:
#     print(b)

# # 64
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# d = a if a < b else b   # a,b 값을 비교 a가 더 작다면 a 출력
# e = d if d < c else c   # d에서 나온 값을 c와 비교 c가 더 작다면 c 출력
# print(e)

# # 65
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a % 2 == 0:
#     print(a)
# if b % 2 == 0:
#     print(b)
# if c % 2 == 0:
#     print(c)

# # 66
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
# if b % 2 == 0:
#     print("even")
# else:
#     print("odd")
# if c % 2 == 0:
#     print("even")
# else:
#     print("odd")

# # 67
# n = int(input())
# if n < 0:
#     if n % 2 == 0:
#         print("A")
#     else:
#         print("B")
# else:
#     if n % 2 == 0:
#         print("C")
#     else:
#         print("D")

# # 68
# n = int(input())
# if n >= 90:
#     print("A")
# elif n >= 70:
#     print("B")
# elif n >= 40:
#     print("C")
# else:
#     print("D")

# # 69
# n = input()
# if n == "A":
#     print("best!!!")
# elif n == "B":
#     print("good!!")
# elif n == "C":
#     print("run!")
# elif n == "D":
#     print("slowly~")
# else:
#     print("what?")

# # 70
# n = int(input())
# if n // 3 == 1:
#     print("spring")
# elif n // 3 == 2:
#     print("summer")
# elif n // 3 == 3:
#     print("fall")
# else:
#     print("winter")

# # 71
# n = 1   # 처음 조건 검사를 통과하기 위해 1로 설정 (While True)
# while True:
#     n = int(input())
#     if n != 0:
#         print(n)
#     else:
#         break

# # 72
# n = int(input())
# while (n!=0):
#     print(n)
#     n -= 1

# # 73
# n = int(input())
# while (n!=0):
#     n -= 1
#     print(n)

# # 74
# c = ord(input())    # 문자를 입력받아 아스키 코드(정수값)으로 변환
# t = ord('a')    # a부터 시작한다고 했으므로 a의 정수값을 t에 저장하기
# while c>=t: # 입력되는 모든 문자가 a와 같거나 a보다는 클 경우(정수로 바꿨을 때)
#     print(chr(t), end=' ')  # 출력하기(뒤에 한칸씩 공백을 두고)
#     t += 1  # 그 다음 문자 출력을 위해 1 더하기(이미 t는 ord 함수를 썼기 때문에 정수값임)

# # 75
# while문으로 풀기
# n=int(input())
# i=0
# while i<=n:
#     print(i)
#     i += 1

# 76
# for문으로 풀기
# n = int(input())
# for i in range(0, n+1):
#     print(i)

# # 77
# n = int(input())
# result = 0
# for i in range(n+1):
#     if i % 2 == 0:
#         result += i
# print(result)









