id_list = list(map(str, input().split()))
report = list(map(str, input().split()))
k = int(input())
print(report)

s = [" ".join(report[i:i+2]) for i in range(0,len(report),2)]
print(s)

report_A = report[0::2] # 신고한 사람
report_B = report[1::2] # 신고당한 사람
print(report_A)
print(report_B)

stop = {}
for i in report_B:    # 각 신고당한 횟수
    try: stop[i] += 1
    except: stop[i] = 1

print(stop)












#dic = {name:value for name, value in zip(report_A,report_B)}
#print(dic)

#report_dict = {report[i]: report[i + 1] for i in range(0, len(report),2)}

