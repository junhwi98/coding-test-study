from collections import Counter

n = int(input())
n_list = list(input().split())

m = int(input())
m_list = list(input().split())

counter = Counter(n_list)
for i in m_list:
    print(counter[i], end=' ')