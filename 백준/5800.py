K = int(input())

save = []

for _ in range(K):

    arr = []
    maxx = 0
    minn = 0

    X = list(map(int, input().split()))

    for i in range(len(X)-1):
        arr.append(X[i+1])

    arr.sort(reverse=True)
    maxx = max(arr)
    minn = min(arr)

    result = 0

    for j in range(len(X)-2):
        result = max(result, abs(arr[j]-arr[j+1]))

    save.append([maxx,minn,result])

for i in range(K):
    print("Class", i+1)
    print("Max", str(save[i][0])+',', "Min", str(save[i][1])+',',
     "Largest gap", save[i][2])

# K = int(input())

# for i in range(K):

#     X = list(map(int, input().split()))
#     del X[0]
#     X.sort()
#     arr = []
#     print('Class', i+1)
#     for i in range(len(X)-1):
#         arr.append(X[i+1] - X[i])

#     print('Max', str(max(X))+',' ,'Min', str(min(X))+',', 'Largest gap', max(arr))