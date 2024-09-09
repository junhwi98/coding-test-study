n, k = map(int, input().split())
value = [ int(input()) for _ in range(n)]
count = 0
value.sort(reverse=True)


for i in value:
    if k >= i:
        count += k // i
        k %= i

        if k <=0:
            break
print(count)