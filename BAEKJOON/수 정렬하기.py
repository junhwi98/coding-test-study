n = int(input())

n_list =  [int(input()) for _ in range(n)]

n_list.sort()
for i in n_list:
    print(i)
    