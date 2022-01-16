### 1. 파이썬이란?
# print("Hello World!!!")


### 2-1. 변수와 자료형
## 10
# x = 1
# y = 2
# print(id(x))
# print(id(y))

## 11
# x = 10
# y = x
# print(id(x))
# print(y)
# print(id(y))

## 12
# x = 10
# y = 10
# z = 20
# print(id(x))
# print(id(y))
# print(id(z))
# y = 20
# print(id(y))

# x = "hello"
# y = "ji yoon"
# z = x
# print(id(x))
# print(id(y))
# print(id(z))

## 13
# a = 3
# b = 2
# print(a+b) 
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a%b)
# print(a//b)

## 14
# a = 4
# print(type(a))
# b = 3.14
# print(type(b))
# print(a+b)
# print(type(a+b))

## 16
# x = 3.14
# print(type(3.14))
# x = int(3.14)
# print(x)
# print(type(x))

# y = 2
# print(type(2))
# y = float(2)
# print(y)
# print(type(y))

## 18
# print(bin(33)) # 2진수
# print(oct(33)) # 8진수
# print(hex(33)) # 16진수

# print(int("0x3837", 16))

## 20
# print('my dog\'s name is happy')
# print("my dog's name \n is happy")
# print("my dog's name \t is happy")

# # 21
# print ("I am "+ "21" + " years old")
# print ("I am "+ str(21) + " years old")
# print("hello " * 10)
# a = "hello"
# print(len(a))   # 5

# # 22
# s = "hello world"
# print(s[:3])

# # 23
# a = "Life is too short, You need Python"
# print(a[19:-7])
# print(a[-1])
# print(a[:])
# print(a[3:])
# print(a[:5])

# # 25
# print("I eat {0} apples".format(3))
# name = "jiyoon"
# print("{0} is so pretty. I like her.".format(name))
# name = "jiyoon"
# age = 21
# print(f"{name} is so pretty. And she is {age} years old.".format(name, age))

# # 26
# print("hello".upper())
# print("HELLO".lower())
# print("hello".find("e"))
# print("good morning".find("or"))
# print("good morning".replace("morning", "evening"))
# print("hi john ".strip())

# # 27
# print("good morning".split())
# print("hi, john".split(','))




# # 숙제 1
# a = 5 ** 8
# print(a)
# print(len(str(a)))