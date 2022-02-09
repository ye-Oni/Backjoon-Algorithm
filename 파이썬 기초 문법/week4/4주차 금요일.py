### 파이썬 코드업 100제 풀이 ###
# # 1
# print("Hello")

# # 2
# print("Hello","World")

# # 3
# print("Hello\nWorld")

# # 4
# print("'Hello'")

# # 5
# print('"Hello World"')

# # 6
# print('"!@#$%^&*()\'')

# # 7
# print("\"C:\Download\\'hello'.py\"")    # 따옴표 앞의 \를 안전하게 출력하기 위해서는 \\로 쓰기

# # 8
# print('print("Hello\\nWorld")') # ""와 ''를 섞어서 쓸 때는 \를 \\로 쓰기

# # 9
# n = input()
# print(n)

# # 10
# n = input()     # n = int(input())
# n = int(n)  
# print(n)

# # 11
# f = input()     # f = float(input())
# f = float(f)
# print(f)

# # 12
# a = input()
# b = input()
# print(a)
# print(b)

# # 13
# a = input()
# b = input()
# print(b)
# print(a)

# # 14
# f = input()
# print(f)
# print(f)
# print(f)

# # 15
# a,b = input().split()
# print(a)
# print(b)

# # 16
# a,b = input().split()
# print(b,a)

# # 17
# s = input()
# print(s,s,s)

# # 18
# a,b = input().split(":")
# print(a,b,sep=':')

# # 19
# y,m,d = input().split(".")
# print(d,m,y,sep="-")

# # 20
# # sep을 활용한 풀이
# a,b = input().split('-')
# print(a,b,sep='')
# # for문을 활용한 풀이     # split으로 하나의 변수에 입력받으면 얘는 자료형이 list가 됨!
# a = input().split('-')
# for i in a:
#     print(i,end="")

# # 21
# # for문을 활용한 풀이
# s = input()
# for i in s:
#     print(i)
# # 리스트의 인덱스를 활용한 풀이 - 총 5자라고 했으므로!
# s = input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

# # 22
# s = input()
# print(s[0:2],s[2:4],s[4:6])

# # 23
# list index 사용
# s = input().split(":")
# print(s[1])
# 각 변수를 다 따로 지정한 방법
# h, m, s = input().split(':')
# print(m)

# # 24
# # sep 함수 사용
# a,b = input().split()
# print(a,b,sep="")
# # 문자열 더하기 사용
# a, b = input().split()
# print(a+b)

# # 25
# a,b = input().split()
# hap = int(a) + int(b)
# print(hap)
# # 풀어쓰기
# a, b = input().split()
# a=int(a)
# b=int(b)
# c=a+b
# print(c)

# # 26
# a = float(input())
# b = float(input())
# print(a+b)

# # 27
# n = int(input())
# print("%x" %n)

# # 28
# n = int(input())
# print("%X" %n)

# # 29
# n = input()
# hex = int(n,16) # 입력된 n을 16진수로 인식해서 변수 hex에 저장
# print("%o" %hex)  # n에 저장되어 있는 값을 8진수 형태로 출력  # oct - 정수를 8진수 문자열로 바꾸어서 출력해주는 함수
# # print(int("11",2))   # 2진수 '11'을 10진수로 = 3
# # print(int("1A",16)) # 16진수 "1A"를 16진수로 = 26

# # 30
# n = ord(input())    # ord - 아스키 코드 값을 돌려주는 함수
# print(n)

# # 31
# n = int(input())
# print(chr(n))   # chr - 아스키 코드에 해당하는 문자 출력

# # 32
# n = int(input())
# print(-n)

# # 33
# n = ord(input())    # 문자 a가 입력되지만 아스키 코드 값으로 인식해야 +1을 해줄 수 있다
# print(chr(n+1))     # +1이 된 아스키 코드 값을 문자로 바꿔주는 함수로 출력해야 문자가 나올 수 있다. 아니면 숫자 나옴\
    
# # 34
# a,b = input().split()
# print(int(a)-int(b))

# # 35
# a,b = input().split()
# print(float(a)*float(b))

# # 36
# w,n = input().split()
# print(w*int(n))

# # 37
# n = int(input())
# s = input()
# print(n*s)

# # 38
# a,b = input().split()
# print(int(a)**int(b))

# # 39
# f1,f2 = input().split()
# print(float(f1)**float(f2))

# # 40
# a,b = input().split()
# print(int(a)//int(b))

# # 41
# a,b = input().split()
# print(int(a)%int(b))