import sys
input = sys.stdin.readline

n = int(input())

dic = {}

for i in range(n):
    a = input()
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

mx = max(dic.values())

res = []

for j in dic:
    if dic[j] == mx:
        res.append(j)

res.sort()
print(res[0])