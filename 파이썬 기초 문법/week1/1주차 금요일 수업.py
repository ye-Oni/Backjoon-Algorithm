# # p.91
# a = {1:'a', 2:'b'}
# print(a[1])
# print(a[2])


# p.93 key,value,item,get,del,clear 실습
# a = {'name':'pey', 'phone' : '0119993323', 'birth' : '1118'}
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a.get('name'))
# print('name' in a)
# print('jiyoon' in a)
# #삭제 메소드
# del a['name']
# print(a)
# a.clear()
# print(a)


# # p.97 set 실습
# s2 = set("hello")
# print(s2)


# # 리스트, 세트 차이점 실습
# alist = list("hello world")
# print(alist)
# alist2 = list(set(alist))
# print(alist2)


# # Quiz
# set1 = set("hello")
# set2 = set("helo")
# print(set1)
# print(set2)


# # bool 자료형
# print(2>1)
# print(2<1)
# print(bool('python'))
# print(bool(''))
# print(bool(1))
# print(bool(0))


# # p.122 조건문 연습
# money = 2000
# if money >= 3000:
# 	print("택시를 타고 가라")
# else:
# 	print("걸어 가라")  


# # 튜플, 리스트, 딕셔너리, 세트
# #튜플
# if (1,2) == (2,1):
#     print("both tuple is same")
# else:
#     print("both tuple is different")
# #리스트
# if [1,2] == [2,1]:
#     print("both list is same")
# else:
#     print("both list is different")
# #딕셔너리
# if {1:'a', 2:'b'} == {2:'b',1:'a'}:
#     print("both dictionary is same")
# else:
#     print("both dictionary is different")
# #세트
# if {1,2} == {2,1}:
#     print("both set is same")
# else:
#     print("both set is different")


# P.124 in/not in 실습
# if 1 in [1,2,3]:
#     print("yes")
# else:
#     print("no")

# if 1 not in [1,2,3]:
#     print("yes")
# else:
#     print("no")
