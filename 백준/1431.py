# 기타의 시리얼 번호 (순서대로 정렬)
# 시리얼 번호는 알파벳 대문자와 숫자 0~9로 이루어져 있음
# A와 B의 길이가 다르면 -> 짧은 것
# 두 개의 길이가 같다면 -> A의 모든 자리수의 합과 B의 합을 비교해서 작은것
# 둘 다 똑같다면 -> 사전순으로 비교(숫자가 알파벳보다 사전순으로 작음)

n = int(input())

def num_sum(string):
    result = 0

    for i in string:
        if i.isdigit():
            result += int(i)

    return result

arr = []
for i in range(n):
    if (n<=1000):
        serial = input()
        
        if len(serial) <= 50:
            arr.append(serial)
            arr.sort(key=lambda x: (len(x), num_sum(x), x))

[print(i) for i in arr]

     
