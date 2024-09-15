n = int(input())

string = [input() for _ in range(n)]

string = set(string)    
string = list(string)

string.sort()
string.sort(key= len)

for i in string:
    print(i)