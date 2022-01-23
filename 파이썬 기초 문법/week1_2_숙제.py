# # 숙제 1
# tp1 = ('이름: ', '학번: ', '전공: ')
# tp2 = ('정지윤', '20210202', '컴퓨터공학과')
# tp3 = tp1, tp2
# print(tp3)
# print(tp3[0][0] + tp3[1][0])
# print(tp3[0][1] + tp3[1][1])
# print(tp3[0][2] + tp3[1][2])


# # 숙제 2
#dic = {'학번' : '20210202', '이름' : '정지윤', '학과' : 'IT학과'}
# print(dic['이름'])
# print(dic['학과'])
# print(dic['학번'])
# print(dic.get('학번'))
# print(dic.get('이름'))
# print(dic.get('학과'))


# # 숙제 3
# A = {1,2,3,4,5}
# B = {3,4,5,6,7}

# print((A | B) - (A & B))

# hap = A.union(B)
# kyo = A.intersection(B)
# print(hap.difference(kyo))


# # 숙제 4
# alist = ['rome', 'paris', 'Beijing', 'Berlin']
# if 'seoul' not in alist:
#     alist.append('seoul')

# print(alist)    


# # 숙제 5
# jiyoon = 1
# if jiyoon == 1:
#     print("예쁘다")
# elif jiyoon == 2:
#     print("안 예쁘다")
# else:
#     print("판단 불가")


### 연습문제 p.112 

# # 8번
# a = (1,2,3)
# a = a + (4,)
# print(a)


# # 10번
# a = {'A':90, 'B':80, 'C':70}
# result = a.pop('B')
# print(a)
# print(result)


# # 11번
# a = [1,1,1,2,2,3,3,3,4,4,5]
# aSet = set(a)
# b = list(aSet)
# print(b)


# # 12번
# a = b = [1,2,3]
# a[1] = 4
# print(b)
# a와 b모두 동일한 리스트 [1,2,3]을 가리키고 있기 때문.


# # p.146 1번
# a = "Life is too short, you need python"

# if "wife" in a:
#     print("wife")
# elif "python" in a and "you" not in a:
#     print("python")
# elif "shirt" not in a:
#     print("shirt")
# elif "need" in a:
#     print("need")
# else:
#     print("none")











# # 랜덤함수 사용하기
# import random
# ran = random.randint(1,10)
# if ran > 5:
#     print("성공")
# else:
#     print("실패")