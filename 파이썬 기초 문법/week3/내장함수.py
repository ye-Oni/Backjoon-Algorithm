## 모든 함수는 '함수이름()' 와 같은 형식으로 작성함

# abs - 절댓값
print(abs(-3))  # 3

# all - 하나라도 거짓이면 False, 모두 참일 때만 True
print(all([1,2,3])) # True   
print(all([0,1,2,3]))   # False

# any - 하나라도 참이면 True, 모두 거짓일 때만 False
print(any([0,1,2,3]))   # True
print(any([0,""]))  # False

# chr - 아스키 코드에 해당하는 문자 출력
print(chr(97))  # a

# dir - 자체적으로 가지고 있는 변수나 함수 출력
print(dir([1,2,3])) # list가 가지고 있는 함수

# divmod(a,b) - a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려줌
print(divmod(7,3))  # (2,1)

# enumerate - 순서가 있는 자료형(리스트, 튜플, 문자열)의 순서를 앞에 붙여서 출력
for i, word in enumerate(["jiyoon","is","pretty"]):
    print(i, word)  # i는 인덱스(순서)를 출력해주고 word는 리스트 안에 있는 값을 출력해줌.
    
# eval - 문자열을 실행한 결괏값을 돌려줌
print(eval("1+2"))  # 3 -> 원래는 1+2가 나와야됨
print("1+2")    # 1+2

# filter - 첫번째 인수로 함수이름, 두번째 인수로 함수에 들어갈 자료형을 입력받음 : 반환 값이 참인 것만 걸러서 돌려주는 함수
def positive(x):
    return x>0
print(list(filter(positive, [1,-3,2,0,-5,6])))  # positive 함수 호출(첫번째 인수), 함수에 들어갈 리스트(두번째 인수)
# lamda
print(list(filter(lambda x:x>0, [1,-3,2,0,-5,6])))  # [1,2,6]

# hex - 정수를 입력받아 16진수로 돌려주는 함수
print(hex(234)) # 0xea

# id - 객체의 고유 주소값을 돌려주는 함수
a = 3
print(id(a))    # 매번 바뀜

# input - 사용자 입력을 받는 함수
# a = input("아무거나 입력하세요 : ")
# print(a)

# int - 문자열 형태의 숫자나 소수점이 있는 숫자등을 정수형태로 돌려주는 함수
print(int("3")) # 3
print(int(3.4)) # 3
# 2,8,16진수로 표현된 값을 10진수로 바꿔서 출력하기
print(int("11",2))   # 2진수 '11'을 10진수로 = 3
print(int("1A",16)) # 16진수 "1A"를 16진수로 = 26

# isinstance - 첫번재 인수로 인스턴스, 두번째 인수로 클래스 이름을 받아 해당 인스턴스가 해당 클래스의 인스턴스라면 True, 아니면 False 반환
class Person:
    pass
a = Person()
print(isinstance(a,Person)) # True
b = 1
print(isinstance(b,Person)) # False

# len - 입력값의 길이를 돌려주는 함수
print(len([1,2,3])) # 3

# list - 특정 자료형을 리스트로 반환해주는 함수
print(list("python"))   # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3)))    # [1,2,3] 튜플을 리스트로 반환

# map - 첫번째 인수에는 함수, 두번째 인수에는 자료형을 입력받아 함수가 수행한 결과를 묶어서 돌려줌
def two_times(x):
    return x*2
print(list(map(two_times, [1,2,3,4])))  # [2, 4, 6, 8]
# lambda
print(list(map(lambda x:x*2, [1,2,3,4])))   # [2, 4, 6, 8]

# max/min - 최댓값, 최솟값을 반환해주는 함수
a = [1,2,3]
print(max(a))   # 3
print(min(a))   # 1

# oct - 정수를 8진수 문자열로 바꾸어서 출력해주는 함수
print(oct(34))  # 0o42

# open - 파일 이름과 읽기 방법을 입력받아 객체를 돌려주는 함수
f = open("write.txt", 'w') # 자동으로 파일 생성

# ord - 아스키 코드 값을 돌려주는 함수
print(ord('a')) # 97

# pow(x,y) - x의 y 제곱한 결과를 돌려주는 함수
print(pow(2,4)) # 16

# range - for문과 함께 사용하는 함수
# 인수가 1개일때
print(list(range(5)))   # [0, 1, 2, 3, 4] : 0부터 시작
# 인수가 2개일때    
print(list(range(2,5))) # [2, 3, 4] : 지정해준 숫자부터 시작
# 인수가 3개일때
print(list(range(1,10,2)))  # [1, 3, 5, 7, 9] : 1부터 9까지, 숫자 사이의 거리는 2

# round - 숫자를 반올림해주는 함수
print(round(4.6))   # 5
print(round(4.2))   # 4
print(round(5.678, 2)) # 5.68 - 소수점 둘째자리(2)에서 반올림

# sorted - 값을 정렬해주는 함수
print(sorted([2,5,4,3,1]))

# str - 문자열 형태로 변환하여 돌려주는 함수
print(str(3))   # '3' => 출력됐을 때는 구분 안가지만 int 3이 str 3으로 바뀜
print(str("hi".upper()))    # 문자열을 대문자로 바꿔주기(upper 함수)    # HI

# sum - 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
print(sum([1,2,3])) # 6
print(sum((1,2,3))) # 6

# tuple - 반복 가능한 자료형을 입력받아 튜플 형태로 돌려주는 함수
print(tuple("abc")) # ('a', 'b', 'c')
print(tuple([1,2,3]))    # (1, 2, 3)

# type - 입력값의 자료형이 무엇인지 알려주는 함수
print(type("abc"))  # <class 'str'>
print(type([1,2,3]))    # <class 'list'>

# zip - 동일한 개수로 이어진 자료형을 묶어주는 함수
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b)))   # [(1, 4), (2, 5), (3, 6)]