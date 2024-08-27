n = int(input())

tile = [0] * n

tile[0] = 1

if n >= 2:
    tile[1] = 2
    for i in range(2, n):
        tile[i] = tile[i-1] + tile[i-2]

print(tile[n-1] % 10007)