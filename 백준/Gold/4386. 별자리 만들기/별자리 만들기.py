import math, sys
input = sys.stdin.readline


def findset(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = findset(parents[x])
        return parents[x]

def union(x, y):
    px, py = findset(x), findset(y)
    if px != py:
        if px < py:
            parents[px] = py
        else:
            parents[py] = px


n = int(input())

arr = []
parents = [x for x in range(n + 1)]
for _ in range(n):
    a, b = map(float, input().split())
    arr.append([a, b])



tmp = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            tmp.append([i, j, math.sqrt((arr[j - 1][0] - arr[i - 1][0]) ** 2 + (arr[j - 1][1] - arr[i - 1][1]) ** 2)])


tmp.sort(key=lambda x: x[2])

cnt = 1
amount = 0

for k in range(len(tmp)):
    if cnt == n:
        break
    if findset(tmp[k][0]) != findset(tmp[k][1]):
        cnt += 1
        amount += tmp[k][2]
        union(tmp[k][0], tmp[k][1])

print(round(amount, 2))