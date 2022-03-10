n = int(input())
alist = []
if (1<=n<=1000):
    for i in range(n):
        num = int(input())
        alist.append(num)
    alist = sorted(alist, reverse=False)
    for i in range(len(alist)):
        print(alist[i])

else:
    print("n의 범위는 1<=N<=1000 입니다.")



# # 버블정렬을 활용한 코드

# N = int(input())

# numbers = []

# for _ in range(N) : 
#     numbers.append(int(input()))

# # Bubble Sort
# for i in range(len(numbers)) : 
#     for j in range(len(numbers)) : 
#         if numbers[i] < numbers[j] : 
#             numbers[i], numbers[j] = numbers[j], numbers[i]
            
# for n in numbers : 
#     print(n)
