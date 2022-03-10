# # 78
# while True:
#     c = input()
#     print(c)
#     if c == 'q':
#         break

# # 79
#for문으로 풀기
# n = int(input())
# result = 0
# for i in range(n):
#     result += i
#     if result >= n:
#         print(i)
#         break
# #while문으로 풀기1
# n = int(input())
# i = 0
# result = 0
# while True:
#     i += 1
#     result += i
#     if result >= n:
#         print(i)
#         break
# #while문으로 풀기2
# n =int(input())
# i = 0
# result = 0
# while result < n:
#     i += 1
#     result += i
# print(i)

# # 80
# n,m = map(int, input().split())
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(i,j)

# # 81
# n = int(input(), 16)
# for i in range(1,16):
#     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# # 82
# n = int(input())
# for i in range(1, n+1) :
#   if i%10==3 or i%10==6 or i%10==9 :
#     print("X", end=' ')
#   else :
#     print(i, end=' ')
# # 풀어쓴 풀이
# n = int(input())
# for i in range(1, n+1):
#     if i % 10 == 3:
#         print('X', end=' ')
#     elif i % 10 == 6:
#         print('X', end=' ')
#     elif i % 10 == 9:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')

# # 83
# r,g,b = map(int, input().split())
# cnt = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i,j,k)
#             cnt += 1
# print(cnt)    # print(r*g*b)

# # 84
# h,b,c,s = map(int, input().split())
# totalBit = h*b*c*s  # 필요한 저장공간의 크기
# totalByte = totalBit/8     # bit를 byte로 바꾸기 위해 8 나누기
# totalKB = totalByte/1024    # byte를 KB로 바꾸기 위해 1024 나누기 (1024Byte = 1KB)
# totalMB = totalKB/1024      # KB를 MB로 바꾸기 위해 1024 나누기 (1024KB = 1MB)
# print(round(totalMB, 1),"MB")   # 소수점 첫째자리에서 반올림한 후 MB를 붙여서 출력해주기
# print(round((h*b*c*s)/8/1024/1024, 1),"MB")  # -> 이만큼의 저장공간이 필요

# # 85
# w,h,b = map(int, input().split())
# print('%.2f'%(w*h*b/8/1024/1024),"MB")

# # 86
# n = int(input())
# i = 0
# result = 0
# while True:
#     i += 1
#     result += i
#     if result >= n:
#         print(result)
#         break

# # 87
# n = int(input())
# for i in range(1, n+1):
#     if i%3 != 0:
#         print(i, end=' ')
# continue 사용하기
# n=int(input())
# for i in range(1, n+1) : 
#   if i%3==0 : 
#     continue            #다음 반복 단계로 넘어간다.
#   print(i, end=' ')    #i가 짝수가 아닐 때만 실행된다.

# # 88
#while문으로 풀기
# a,d,n = map(int, input().split())
# c = 1   # 이미 첫 시작값 a가 첫번째 수이기 때문에 그 다음은 2번재 수라는 것!
# while c < n:
#     a += d
#     c += 1
# print(a)
#for문으로 풀기
# a,d,n = map(int, input().split())
# s=a
# for i in range(2, n+1):
#    s += d
# print(s) 

# 89
#for문으로 풀기
# a,r,n = map(int, input().split())
# s = a
# for i in range(2, n+1):
#     s*=r
# print(s)
#while문으로 풀기
# a,r,n = map(int, input().split())
# c=1
# while c<n:
#     a*=r
#     c+=1
# print(a)

# # 90
# #for문으로 풀기
# a,m,d,n = map(int, input().split())
# s=a
# for i in range(2, n+1):
#     s = s*m+d
# print(s)
# #while문으로 풀기
# a,m,d,n = map(int, input().split())
# c=1
# while c<n:
#     a*=m
#     a+=d
#     c+=1
# print(a)

# # 91
# a,b,c = map(int, input().split())
# d=1
# while True:
#     if d%a==0 and d%b==0 and d%c==0:
#         break
#     d+=1
# print(d)

# # 92
#내 풀이
# n = int(input())
# r = list(map(int, input().split()))
# result = [0] * 23
# for i in range(23): # 1~23이기 때문
#     cnt = 0
#     for j in range(n):
#         if r[j] == i+1:
#             cnt +=1
#     result[i] = cnt
# for i in result:
# #     print(i, end=' ')
# #답안
# n = int(input())
# r = list(map(int, input().split()))
# result = [0] * 24   # 0부터 23번째까지(인덱스) 저장됨
# for i in range(n):
#     result[r[i]] += 1
# for i in range(1,24):   # 첫번째 요소부터 출력해야함(0번은 없기 때문) -> 1~23
#     print(result[i], end=' ')

# # 93
# # 내풀이
# n = int(input())
# k = list(map(int, input().split()))
# k.reverse()
# for i in k:
#     print(i, end=' ')
# #다른풀이
# n = int(input())
# k = list(map(int, input().split()))
# for i in range(n-1, -1, -1):
#   print(k[i], end=' ')

# # 94
# #내풀이
# n = int(input())
# k = list(map(int, input().split()))
# k.sort()
# print(k[0])
# #다른풀이
# n = int(input())
# k = list(map(int, input().split()))
# min = k[0]  # 일단 최솟값을 가장 첫번째 요소로 두기
# for i in range(0,n):
#     if k[i] < min:  # k안의 원소를 살펴보다가 처음 min보다 더 작은 값이 있으면 그걸 최솟값으로 바꾸기
#         min = k[i]
# print(min)

# 95
n = int(input())
arr = [[0] * 19] * 19
print(arr)
for i in range(n):
    x,y = map(int, input().split())




