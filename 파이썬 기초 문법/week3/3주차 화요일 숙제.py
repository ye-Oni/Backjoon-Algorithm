


# # P.262 연습문제
# Q1
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


# # Q2
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = "100 이상의 값은 가질 수 없습니다."
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(50)

# print(cal.value)