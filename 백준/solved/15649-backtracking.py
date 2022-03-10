# 백트래킹의 특징 : N이 작음(N이 10근처여야 사용가능함.)
# => 재귀함수를 사용할 때, 종료 시점 잊지말기!!!

# 1. 아이디어
# - 백트래킹 재귀함수 안에서, for문을 돌면서 1부터 N중에서 숫자를 하나 선택
# - 다음 1부터 N까지 선택할 때, 이미 선택한 값이 아닌 경우 선택(방문여부 체크)
# - 재귀함수에서 M개를 선택할 경우 출력

# 2. 시간복잡도
# - N^N : 중복이 가능, N = 8 까지 가능
# - N! : 중복이 불가, N = 10 까지 가능
# 이 문제에서는 N의 최댓값이 8이기 때문에 백트래킹이 가능함.

# 3. 자료구조
# - 방문 여부 확인 배열 : bool[]
# - 선택한 값 입력 배열(결과값 저장) : int[]



import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
 
result = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(1,n+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()
 
dfs()



# 다른 풀이

N,M = map(int, input().split())
result = []
chk = [False] * (N+1) # 인덱스 값이 0이기 때문에 N보다 1크게 설정해주기(범위가 0부터 N-1이기 때문에 1~N까지 사용할 수 있도록 N+1만큼 곱해줌)

def recur(num):
    if num == M:
        print(' '.join(map(str, result)))   # result를 string으로 바꾼 후, 각각 배열에 있는 값을 한 칸 공백을 두고 join 해서 출력
        return
    for i in range(1, N+1):  # 위에 [False]를 N+1만큼 곱해준 것과 같은 원리
        if chk[i] == False:
            chk[i] = True
            result.append(i)
            recur(num+1)
            chk[i] = False
            result.pop()    # 마지막 값을 제거해줌
            
recur(0)