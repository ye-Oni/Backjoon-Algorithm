### 2-2. 리스트

# # 36
# myVisitCities = ["seoul", "paris", "new York", "bali", "Lodon" ]
# print(myVisitCities[-1])
# print(myVisitCities.remove("seoul"))
# del myVisitCities[2]
# print(myVisitCities)

# myVisitCities = ["seoul", "paris", "new York", "bali", "Lodon" ]
# print(myVisitCities.pop())
# print(myVisitCities.pop(2))

# # 44
# alist = [1,3,2]
# alist.reverse()
# print(alist)

# # 45
# alist = [2,4,5,1,3]
# # 메소드 사용
# print(alist.sort())
# alist.sort()
# print(alist)
# # 함수 사용
# sorted(alist)
# print(alist)
# print(sorted(alist))


# # 숙제 2
# alist = [1,2,4,6]
# alist.insert(2, 3)
# alist.insert(4, 5)
# print(alist)


# # 숙제 3
# alist = ['seoul', 'rome', 'paris', 'Beijing', 'Berlin', 'seoul'] 
# print(alist.index('seoul'))
# print(alist.count('seoul'))

# # 숙제 4
# tp1 = ('이름: ', '학번: ', '전공: ')
# tp2 = ('정지윤', '20210202', '컴퓨터공학과')
# tp3 = tp1, tp2
# print(tp3)
# print(tp3[0][0] + tp3[1][0])
# print(tp3[0][1] + tp3[1][1])
# print(tp3[0][2] + tp3[1][2])