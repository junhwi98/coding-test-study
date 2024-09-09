n = int(input())
p = list(map(int, input().split()))
sum = 0
p.sort()

for i in range(n):
    sum += p[i]
    if i >= 1:
        for j in range(0, i):
            sum += p[j]
print(sum) 