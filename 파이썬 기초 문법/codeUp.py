# 코드업 100제 풀이

#7
#print('print(\"Hello\\nWorld\")')

#9
#c = input("문자 1개 입력: ")
#print(c)

#10
# n = input()
# n = int(n)
# print(n)

#11
# f = input()
# f = float(f)
# print(f)

#12
# a = input()
# b = input()
# print(a)
# print(b)

#13
# a = input()
# b = input()
# print(b)
# print(a)

#14
# a = input()
# a = float(a)
# for i in range(3):
#     print(a)

#15
# a,b = input().split()
# print(a)
# print(b)

#16
# a,b = input().split()
# print(b, a)

#17
# s = input()
# print(s, s, s)

#18
# a,b = input().split(':')
# print(a,b,sep=':')

#19
# y,m,d = input().split('.')
# print(d,m,y,sep='-')

#20
# a,b = input().split('-')
# print(a,b,sep="")

#21
# s = input()
# for i in range(5):
#     print(s[i])

#22
# s = input()
# print(s[0:2], s[2:4], s[4:6])

#23
# s = input().split(":")
# print(s[1])

#24
# w1,w2 = input().split()
# s = w1 + w2
# print(s)

#25
# a,b = input().split()
# c = int(a) + int(b)
# print(c)

#26
# a = input()
# b = input()
# c = float(a) + float(b)
# print(c)

#27
# a = input()
# n = int(a)
# print('%x'% n)

#28
# a = input()
# n = int(a)
# print('%X'% n)

#29
# a = input()
# n = int(a, 16)
# print('%o'% n)

#30
# n = ord(input())
# print(n)

#31
# c = int(input())
# print(chr(c))

#32
# n = int(input())
# print(-n)

#33
# n = ord(input())
# print(chr(n+1))

#34
# a,b = input().split()
# c = int(a) - int(b)
# print(c)

#35
# a,b = input().split()
# c = float(a) * float(b)
# print(c)

#36
# w,n = input().split()
# print(w*int(n))

#37
# n = input()
# s = input()
# print(int(n)*s)

#38
# a,b = input().split()
# c = int(a)**int(b)
# print(c)

#39
# f1,f2 = input().split()
# c = float(f1)**float(f2)
# print(c)

#40
# a,b = input().split()
# print(int(a)//int(b))

#41
# a,b = input().split()
# print(int(a)%int(b))

#42
# a = float(input())
# print(format(a, ".2f"))

# a = float(input())
# print(round(a,2))

#43
# f1,f2 = input().split()
# f3 = float(f1)/float(f2)
# print(format(f3, ".3f"))

#44
# a,b = input().split()
# print(int(a)+int(b))
# print(int(a)-int(b))
# print(int(a)*int(b))
# print(int(a)//int(b))
# print(int(a)%int(b))
# print(format(int(a)/int(b), ".2f"))

#45
# a,b,c = input().split()
# s = int(a)+int(b)+int(c)
# a = s / 3
# print(s, format(a, ".2f"))

#46
# n = int(input())
# print(n<<1)

#47
# a,b = input().split()
# print(int(a)<<int(b))

#48
# a,b = input().split()
# print(int(a) < int(b))

#49
# a,b = input().split()
# print(int(a)==int(b))

#50
# a,b = input().split()
# print(int(b)>=int(a))

#51
# a,b = input().split()
# print(int(a)!=int(b))

#52
# n = int(input())
# print(bool(n))

#53
# a = bool(int(input()))
# print(not a)

#54
# 둘다 참일 경우 -> 참
# a,b = input().split()
# print(bool(int(a) and bool(int(b))))

#55
# 하나라도 참이면 -> 참
# a,b = input().split()
# print(bool(int(a) or bool(int(b))))

#56
# 참, 거짓이 서로 다를 때만 참
# a,b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# print((a and (not b)) or ((not a) and b))

#57
# 참, 거짓이 서로 같을 때만 참
# a,b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# print(((not a) and (not b)) or (a and b))

#58
# 둘다 거짓일 경우만 참
# a,b = input().split()
# a = bool(int(a))
# b = bool(int(b))
# #print((not a) and (not b))
# print(not(a or b))

#59
# a = int(input())
# print(~a)

#60
# a,b = input().split()
# print(int(a) & int(b))

#61
# a,b = input().split()
# print(int(a) | int(b))

#62
# a,b = input().split()
# print(int(a) ^ int(b))

#63
# a,b = input().split()
# a = int(a)
# b = int(b)
# c = (a if(a>=b) else b)
# print(int(c))

#64
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# n = (a if(a<b) else b) if ((a if a<b else b)<c) else c
# print(int(n))

#65
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a%2 == 0:
#     print(a)
# if b%2 == 0:
#     print(b)
# if c%2 == 0:
#     print(c)

#66
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# d = [a,b,c]
# for i in d:
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")
# if a%2==0:
#     print("even")
# else:
#     print("odd")
# if b%2==0:
#     print("even")
# else:
#     print("odd") 
# if c%2==0:
#     print("even")
# else:
#     print("odd")  

#67
# n = int(input())
# if n<0:
#     if(n%2 == 0):
#         print("A")
#     else:
#         print("B")
# else:
#     if(n%2 == 0):
#         print("C")
#     else:
#         print("D")

#68
# n = int(input())
# if n>=90:
#     print("A")
# elif n>=70:
#     print("B")
# elif n>=40:
#     print("C")
# else:
#     print("D")

#69
# n = input()
# if n == 'A':
#     print("best!!!")
# elif n == 'B':
#     print("good!!")
# elif n == 'C':
#     print("run!")
# elif n == 'D':
#     print("slowly~")
# else:
#     print("what?")

#70
# n = int(input())
# if (n>0 and n<13):
#     if (n!=12) and n//9 == 1:
#         print("fall")
#     elif n//3 == 1:
#         print("spring")
#     elif n//6 == 1:
#         print("summer")
#     else:
#         print("winter")

#71
# n = 1
# while n!=0:
#     n = int(input())
#     if n!=0:
#         print(n)

#72
# n = 1
# while (n!=0) and (n <= 100):
#     n = int(input())
#     print(n)
#     for i in range(n-1):
#         n = n - 1
#         print(n)

#73
# n = 1
# while(n!=0) and (n<=100):
#     n = int(input())
#     for i in range(n):
#         n-=1
#         print(n)

#74
# c = ord(input())
# t = ord('a')
# while t<=c:
#     print(chr(t), end=' ')
#     t+=1

#75
# n = int(input())
# a = 0
# while a<=n:
#     print(int(a))
#     a+=1

#76
# n = int(input())
# for i in range(n+1):
#     print(i)

#77
# n = int(input())
# s = 0
# for i in range(1, n+1):
#     if i%2==0:
#         s+=i
# print(s)

#78
# while(True):
#     n = input()
#     if n == 'q':
#         print(n)
#         break
#     print(n)

#79
# n = int(input())
# s = 0
# for i in range(1000):
#     s+=i
#     if s>=n:
#         print(i)
#         break

#80
# n,m = input().split()
# m = int(m)
# n = int(n)
# if (m<=10) and (n<=10):
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             print(i,j)

#81
# n = int(input(),16)
# for i in range(1,16):
#     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#82
# n = int(input())
# if n<30:
#     for i in range(1, n+1):
#         if i%10==3:
#             print("X", end=' ')
#         elif i%10==6:
#             print("X", end=' ')
#         elif i%10==9:
#             print("X", end=' ')
#         else:
#             print(i, end=' ')

#83
# r,g,b = input().split()
# r = int(r)
# g = int(g)
# b = int(b)
# count = 0
# for i in range(0,r):
#     for j in range(0,g):
#         for k in range(0,b):
#             print(i, j, k)
#             count+=1
# print(count)

#20s code
# a="*"
# for i in range(1,6):
#     print(i*a)
#one2ye code
# for i in range(6):
#     print(i*"*")

#다중 for문 - 별
# for i in range(5):
#     for j in range(i+1):
#         print('*', end="")
#     print('')
#다중 for문 - 별 거꾸로
# for i in range(5,0,-1):
#     for j in range(i):
#         print('*', end="")
#     print('')

#84
#h: 1초동안 마이크로 소리강약을 체크하는 횟수
#b: 한번 체크한 값을 저장할때 사용하는 비트수
#c: 좌우 소리를 저장할 트랙개수인 채널 개수
#s: 녹음할 시간(초)
# h,b,c,s = input().split()
# h = int(h)
# b = int(b)
# c = int(c)
# s = int(s)
# if (0<h<=48000) and ((0<b<=32) and (b%8==0)) and (0<c<=5) and (0<s<=6000):
#     result = float(h*b*c*s/8/1024/1024)
#     a = format((result), ".1f")
#     print(a, end=" ")
#     print("MB")
    #print((format(float(h*b*c*s/8/1024/1024))), ".1f")

#85
# w,h,b = input().split()
# w = int(w)
# h = int(h)
# b = int(b)
# if (0<w,h<1024) and (b%4==0 and b<=40):
#     print('%.2f'% float((w*h*b/8/1024/1024)), end=' ')
#     print('MB')

#86
# n = int(input())
# sum = 0
# for i in range(n+1):
#     sum = sum + i
#     if sum>=n:
#         break
# print(sum)

#87
# n = int(input())
# for i in range(1, n+1):
#     if i%3==0:
#         continue
#     print(i, end=' ')

# 88
# a, d, n = input().split()
# a = int(a)
# d = int(d)
# n = int(n)
# count = 0
# for i in range(n-1):
#     count += 1
#     a = a + d
#     if count == n:
#         break
# print(a)

# 89
# a,r,n = input().split()
# a = int(a)
# r = int(r)
# n = int(n)
# count = 0
# if (0<=a,r,n<=10):
#     for i in range(n-1):
#         count += 1
#         a = a * r
#         if count == n:
#             break
# print(a)

#90
# a,m,d,n = input().split()
# a = int(a)
# m = int(m)
# d = int(d)
# n = int(n)
# count = 0
# if (-50<=a,m,d<=50) and (0<n<=10):
#     for i in range(n-1):
#         count += 1
#         a = a*m+d
#         if count == n:
#             break
# print(a)

#91
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# day = 1
# if (0<a,b,c<=100):
#     while day%a!=0 or day%b!=0 or day%c!=0:
#         day+=1
# print(day) 

#92
# n = int(input())
# a = input().split()
# for i in range(n):
#     a[i] = int(a[i])
# d=[]
# for i in range(24):
#     d.append(0)
# for i in range(n):
#     d[a[i]]+=1
# for i in range(1,24):
#     print(d[i], end=' ')

#93
# n = int(input())
# k = input().split()
# if (0<n<=10000):
#     for i in range(n):
#         k[i] = int(k[i])
#     for i in range(n-1,-1,-1):
#         print(k[i], end=' ')

#94
# n = int(input())
# k = input().split()
# if (0<n<=10000):
#     for i in range(n):
#         k[i] = int(k[i])
# k.sort()
# print(k[0])

#95
# d = []
# for i in range(20):
#     d.append([])
#     for j in range(20):
#         d[i].append(0)
# # d = [[0 for j in range(20)] for i in range(20)]
# n = int(input())
# if (0<n<=10):
#     for i in range(n):
#         x,y = input().split()
#         d[int(x)][int(y)] = 1
#     for i in range(1,20):
#         for j in range(1,20):
#             print(d[i][j], end=' ')
#         print()

#96
# d = [[0 for j in range(20)] for i in range(20)]
# for i in range(19):
#     a = input().split()
#     for j in range(19):
#         d[i+1][j+1] = int(a[j])
# n = int(input())
# for i in range(n):
#     x,y = input().split()
#     for j in range(1,20):
#         if d[j][int(y)]==0:
#             d[j][int(y)]=1
#         else:
#             d[j][int(y)]=0
#         if d[int(x)][j]==0:
#             d[int(x)][j]=1
#         else:
#             d[int(x)][j]=0
# for i in range(1,20):
#     for j in range(1,20):
#         print(d[i][j], end=' ')
#     print()

# array = [[0 for col in range(11)] for row in range(10)]
# #print(array)
# array[3][1]="@"
# print(array)

# #97
# h,w = input().split()
# h = int(h)
# w = int(w)
# m = []
# m = [[0 for j in range(w+1)] for i in range(h+1)]
# n = int(input())
# for i in range(n):
#     l,d,x,y = input().split()
#     if int(d)==0:
#         for j in range(int(l)):
#             m[int(x)][int(y)+j]=1
#     else:
#         for j in range(int(l)):
#             m[int(x)+j][int(y)]=1
# for i in range(1, h+1):
#     for j in range(1, w+1):
#         print(m[i][j], end=' ')
#     print()



# #98
# m=[] 
# for i in range(12) : 
#      m.append([]) 
#      for j in range(12) : 
#           m[i].append(0) 
# for i in range(10) : 
#      a=input().split() 
#      for j in range(10) : 
#           m[i+1][j+1]=int(a[j]) 
# x = 2 
# y = 2 
# while True : 
#      if m[x][y] == 0 : 
#           m[x][y] = 9 
#      elif m[x][y] == 2 : 
#           m[x][y] = 9 
#           break 
#      if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) : 
#           break 
#      if m[x][y+1] != 1 : 
#           y += 1 
#      elif m[x+1][y] != 1 : 
#           x += 1 
# for i in range(1, 11) : 
#      for j in range(1, 11) : 
#           print(m[i][j], end=' ') 
#      print()