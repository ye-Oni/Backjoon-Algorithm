# # # 숙제 1
# class Vehicle:
#     def __init__(self, speed, color):
#         self.speed = speed
#         self.color = color
#     def __str__(self):
#         return "자동차의 속도는 " + str(self.speed) + ", 자동차의 색깔은 " + self.color

# v1 = Vehicle(120, 'red')
# print(v1)



# # P.262 연습문제
# # Q1
# class Calculator:
#     def __init__(self):
#         self.value = 0
#     def add(self, val):
#         self.value += val

# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val
        
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# cal.add(3)
# cal.minus(9)                                                

# print(cal.value)


#  Q2
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = "100 이상의 값은 가질 수 없습니다."
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(50)

# print(cal.value)#


# # Q4
# a = list(filter(lambda x:x>0, [1,-2,3,-5,8,-3]))
# print(a)


# # Q6
# a = list(map(lambda x:x*3, [1,2,3,4]))
# print(a)


# # Q7
# a = [-8,2,7,5,-3,5,0,1]
# print(max(a))
# print(min(a))
# hap = max(a) + min(a)
# print(hap)


# # Q13
# import random
# result = []
# for i in range(6): 
#     num = random.randint(1,45)
#     result.append(num)
# print(result)