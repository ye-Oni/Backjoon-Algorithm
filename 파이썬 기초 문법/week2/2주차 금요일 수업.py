####### 함수 실습 #######
# # 함수
# def add(a,b):   # a,b는 매개변수
#     result = a + b
#     return result

# print(add(3,4)) # 3,4는 인수


# # 입력 값이 없는 함수
# def say():
#     return 'Hi'
# a = say()
# print(a)

# # # 결과 값이 없는 함수
# def add(a,b):
#     print(a+b)
# add(3,4)
# print(add(3,4))

# # 입력값도 결과값도 없는 함수
# def say():
#     print('Hi')
# say()


# # 매개변수 지정하여 호출
# def add(a,b):
#     return a + b
# result = add(a=3, b=7)
# print(result)

# # 매개변수에 초깃값을 미리 설정하기
# def add(a=3, b=7):
#     return a+b
# print(add())

# # 여러개의 입력값을 받는 함수
# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result   # 입력값과 결과값 모두 있는 함수
# result2 = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result2)

# print(add_many(1,2,3))
# print(add_many(1,2,3,4,5,6,7,8,9,10))

# # 키워드 파라미터
# def print_kwargs(**kwargs):
#     print(kwargs)   # 결과값이 없는 함수
# print_kwargs(a=1)


# # filter 함수
# f = filter(lambda x:x%2, range(10))
# print(list(f))



# 파일 입출력

# #현재 열려있는 디렉토리에 파일 생성하기 & 파일 쓰기
# f = open("파일생성.txt", "w")
# f.write("hello world")
# f.close
# #특정 디렉토리에 파일 생성하기
# f = open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/특정_파일생성.txt", 'w')
# f.close

# # 파일을 쓰기 모드로 열어 출력값 적기
# f = open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/파일쓰기.txt", 'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()

# # 파일의 마지막에 새로운 내용 추가하기
# f = open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/파일쓰기.txt", "a")
# f.write("파이썬은 정말 재밌습니다~!")
# f.close()


# # readline 파일 읽기
# f = open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/파일쓰기.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# # readlines 파일 읽기
# f = open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/파일쓰기.txt", 'r')
# line = f.readlines()
# print(line)
# f.close()

# # read 파일 읽기
# f = open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/파일쓰기.txt", 'r')
# line = f.read()
# print(line)
# f.close()


# # with로 파일 열고 닫기 한번에 하기
# with open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/특정_파일생성.txt", 'w') as fh:
#     fh.write("Jiyoon is so pretty!!")


# # 사칙연산 클래스 만들기
# class FourCal:
#     def setdata(self, first, second):   # 메서드의 매개변수
#         self.first = first  # 메서드의 수행문 1
#         self.second = second    # 메서드의 수행문 2
#     def add(self):  # 더하기
#         result = self.first + self.second
#         return result
#     def sub(self):  # 빼기
#         result = self.first - self.second
#         return result
#     def mul(self):  # 곱하기
#         result = self.first * self.second
#         return result
#     def div(self):  # 나누기
#         result = self.first / self.second
#         return result
# a = FourCal()   # 객체 a
# b = FourCal()   # 객체 b
# # setdata
# a.setdata(4,2)
# b.setdata(3,8)
# print(a.first)  # 4
# print(a.second) # 2
# print(b.first)  # 3
# print(b.second) # 8
# # add
# print(a.add())  # 6
# print(b.add())  # 11
# # sub
# print(a.sub())  # 2
# print(b.sub())  # -5
# # mul
# print(a.mul())  # 8
# print(b.mul())  # 24
# # div
# print(a.div())  # 2.0
# print(b.div())  # 0.375

# # 생성자
# class FourCal:
#     def __init__(self, first, second):   # 생성자
#         self.first = first  
#         self.second = second    
#     def add(self):  # 더하기
#         result = self.first + self.second
#         return result
#     def sub(self):  # 빼기
#         result = self.first - self.second
#         return result
#     def mul(self):  # 곱하기
#         result = self.first * self.second
#         return result
#     def div(self):  # 나누기
#         result = self.first / self.second
#         return result
# a = FourCal(4,2)   # 객체 a
# b = FourCal(3,8)   # 객체 b
# # add
# print(a.add())  # 6
# print(b.add())  # 11
# # sub
# print(a.sub())  # 2
# print(b.sub())  # -5
# # mul
# print(a.mul())  # 8
# print(b.mul())  # 24
# # div
# print(a.div())  # 2.0
# print(b.div())  # 0.375


# # 상속
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
# a = MoreFourCal(4,2)
# print(a.pow())


# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result/len(args)

# print(avg_numbers(1,4))

