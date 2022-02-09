# # 번개 퀴즈 1
A = [1,2,3,4,5,6,7,8,9,10]
# a = sum(A)
# b = a/len(A)
# print("합:", a)
# print("평균:", b)

#  번개 퀴즈 2
result = list(filter(lambda x:x%2==0, A))
print(result)

# 번개 퀴즈 3
result = list(map(lambda x:x**2, A))
print(result)


# # 예외처리
# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

# 복수 예외처리
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

# # 오류 일부러 발생시키기
# class Bird:
#     def fly(self):
#         raise NotImplementedError
# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()

# # 예외 만들기
# class MyError(Exception):   # 파이썬 내장 클래스인 Exceprion 클래스 정의
#     pass       # 내부 동작이 필요없고 의미적으로 껍데기만 필요한 경우에 선언
# # if, 예외처리문에서 사용하는 pass는 오류가 발생하는 상황이 오더라도 그냥 통과시키기 위한 용도 - 주의해서 써야함!

# def say_nick(nick):     # say_nick 이라는 함수 선언
#     if nick == "바보":  # 만약 매개변수인 nick이 바보라면
#         raise MyError() # 위에서 선언한 MyError 발생시킴
#     print(nick)
# try:    
#     say_nick("천사")    # 천사라는 인수를 넣어 함수 say_nick() 호출
#     say_nick("바보")    
# except MyError:
#     print("허용되지 않는 별명입니다")   # 인수에 바보가 들어갈 경우 출력


# 라이브러리 - vsCode 에서 실행할 때는 print문을 사용해서 출력
# # time
# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)

# # 달력
# import calendar
# print(calendar.calendar(2022))

## random
# import random
# # print(random.randint(1,10))

# def random_pop(data):
#     number = random.randint(0, len(data)-1) # 리스트의 인덱스는 0부터 시작하므로 1을 빼주기
#     return data.pop(number) # 뽑힌 리스트 요소의 값은 pop 함수를 사용해서 제거해주기

# if __name__ == "__main__":  # 모듈 자동 실행 방지 함수
#     data = [1, 2, 3, 4, 5]
#     while data: 
#         print(random_pop(data))