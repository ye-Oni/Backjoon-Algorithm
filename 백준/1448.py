N = int(input())

arr = []
[ arr.append(int(input())) for _ in range(N) ]
arr.sort(reverse=True)

# triangle = []
# while True:
#     triangle = arr[:3]
#     del arr[:3]
#     if len(arr) == 0 and triangle[1] + triangle[2] <= triangle[0]:
#         print('-1')
#     if triangle[1] + triangle[2] > triangle[0]:
#         print(sum(triangle))
#         break
#     else:
#         for i in range(len(arr)):
#             del triangle[0]
#             triangle.append(arr[0])
#             del arr[0]
#             if triangle[1] + triangle[2] > triangle[0]:
#                 print(sum(triangle))
#                 break
#     break

isTrue = 0
for i in range(len(arr)-2):
    if arr[i] < arr[i+1] + arr[i+2]:
        print(arr[i] + arr[i+1] + arr[i+2])
        isTrue = 1
        break
if isTrue == 0:
    print(-1)