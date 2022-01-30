# # while문 만들기
# treeHit = 0     # 나무를 찍은 횟수

# while treeHit < 10:     # 나무를 찍은 횟수가 10보다 작은 동안 반복
#     treeHit = treeHit + 1   # 나무를 찍은 횟수 1씩 증가
#     print("나무를 %d번 찍었습니다." %treeHit)   # 숫자를 바로 대입하는 문자열 포맷팅 사용
#     if treeHit == 10:   # 만약 treeHit라는 변수가 10일경우 다음과 같은 메세지 출력
#         print("나무 넘어갑니다.")


# # sentinel & break 문 연습
# a = 0
# while a < 5:
#     a = a + 1
#     if a % 4 == 0:
#         break
#     print("number is ", a)


# continue
# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0:
#         continue
#     else:
#         print

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 3 == 0:
#         print(a)
#     else:
#         continue


# # 무한루프 실습
# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

# # for문 실습
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     if i == 'two':
#         continue
#     else:
#         print(i)


# # range 함수
# for i in range(1,10,2):
#     print(i)

# add = 0
# for i in range(1,11):
#     add = add + i
    
# print(add)


# list comprehension
# 1. 일반적인 for문 사용 방식
# a = [1,2,3,4]
# result = []
# for i in a:
#     result.append(i*3)

# print(result)

# # 2. list comprehension 사용 방식
# a = [1,2,3,4]
# result = [i*3 for i in a]
# print(result)


# # input 함수
# number = input("숫자를 입력하세요 : ")
# print(number)

# name,age = input("이름과 나이를 입력해주세요 : ").split()
# print(name,"님의 나이는",age,"세 입니다.")

# # input 함수 실습
# a,b = input("두 개의 숫자를 입력해주세요: ").split()
# print("결과:",int(a)*int(b))

