T = int(input())

for _ in range(T):
    n = int(input())
    n_0, n_1 = 1, 0

    for i in range(n):
        n_0, n_1 = n_1, (n_0+n_1)
    print(n_0, n_1)
##주석