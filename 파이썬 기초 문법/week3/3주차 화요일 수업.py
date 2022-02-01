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



# # 모듈
# import mod1     # 모듈 임포트
# print(mod1.add(3,4))
# print(mod1.sub(7,4))    # 반드시 함수 앞에 모듈 이름을 붙여주어야 함.

# from mod1 import add    # 모듈의 특정 함수만 사용
# print(add(3,4))     # 함수 앞에 모듈 이름을 붙일 필요가 없음.

# from mod1 import*       # 여러 개의 모듈 임포트
# from mod1 import add
# print(add(3,4))
# print(sub(7,4))

# import mod2
# print(mod2.PI)  # 변수 PI 호출
# a = mod2.Math() # Math 클래스 객체 생성
# print(a.solv(2))    # Math 클래스 안의 solv 함수를 이용해서 원의 넓이 구하기


