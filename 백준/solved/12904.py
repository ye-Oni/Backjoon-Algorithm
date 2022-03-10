S = list(input())
T = list(input())

while True: # True 대신 밑에 조건문을 바로 써서 break문 없이 쓸 수도 있음.
    if len(S) != len(T):
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            T.reverse() # T[::-1]로도 쓸 수 있음.
    else:
        break

if S == T:
    print('1')
else:
    print('0')
# print(1 if S == T else 0)으로 간단하게 쓸 수도 있음.
