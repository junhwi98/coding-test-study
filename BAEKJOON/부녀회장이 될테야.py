T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    zero = [i for i in range(1, n+1)]
    
    for k in range(k):
        for i in range(1, n):
            zero[i] += zero[i-1]
    print(zero[n-1])