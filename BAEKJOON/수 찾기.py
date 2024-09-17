n = int(input())
n_list = list(input().split())

m = int(input())
m_list = list(input().split())
n_list.sort()

def binarysearch(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True
        elif n_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

for i in range(m):
    if binarysearch(m_list[i]):
        print(1)
    else:
        print(0)