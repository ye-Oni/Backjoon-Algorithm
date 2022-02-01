# # # 숙제 1
# def big(*args):
#     return max(args)

# a,b,c = input("3개의 숫자를 입력해주세요: ").split()
# print(big(a,b,c))


# # 숙제 2
# goal = input("새해 목표를 입력해주세요 : ")
# with open ("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/숙제2.txt", "w") as f:
#     f.write(goal)
# with open ("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/숙제2.txt", "r") as f:
#     line = f.readline()
# print(line)
   
    
# # 숙제 3
# id= input("아이디를 입력하세요 : ")
# pw = input("비밀번호를 입력하세요 : ") 
# with open ("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/숙제3.txt", "w") as f:
#     f.write(id)
#     f.write("\n")
#     f.write(pw)
# with open ("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/숙제3.txt", "r") as f:
#     line = f.read()
# print(line)


        

# # 연습문제 2
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result / len(args)

# print(avg_numbers(1,2))
# print(avg_numbers(1,2,3,4,5))


# 연습문제 P.180~181
# Q5
# f1 = open("test.txt","w")
# f1.write("Life is too short")
# f1.close()  # 반드시 파일을 닫아주기
# f2 = open("test.txt", "r")
# print(f2.read())
# f2.close()

# # Q6
# user_input = input("저장할 내용을 입력하세요: ")
# f = open("test.txt", "a")
# f.write(user_input)
# f.write("\n")
# f.close()

# # Q7
# f = open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/Q7.txt", "r")
# body = f.read()
# f.close()

# body = body.replace("java","python")

# f = open("C:/Users/k0305/OneDrive/바탕 화면/Python/파이썬 기초 문법/week2/Q7.txt", "w")
# f.write(body)
# f.close()




