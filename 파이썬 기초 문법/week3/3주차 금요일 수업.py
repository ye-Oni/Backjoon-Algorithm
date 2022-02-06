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



# # 패키지
# import game.sound.echo  # echo 모듈을 실행
# game.sound.echo.echo_test()     # 함수의 리턴값이 없기 때문에 바로 출력 가능

# from game.sound import echo # echo 모듈이 있는 디렉토리까지 from...import 하여 실행
# echo.echo_test()


# from game.sound.echo import echo_test   # echo 모듈의 echo_test 함수를 직접 import 하여 실행
# echo_test()

# # relative
# from game.graphic.render import render_test
# render_test()



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