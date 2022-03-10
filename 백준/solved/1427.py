n = int(input())

n_list = list(map(int, str(n)))
n_list = sorted(n_list, reverse=True)

for i in range(len(n_list)):
    print(n_list[i], end='')

