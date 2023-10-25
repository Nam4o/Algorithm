import sys
input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find_set(parents[x])
        return parents[x]


def union(x, y):
    px, py = find_set(x), find_set(y)
    if px != py:
        if px < py:
            parents[px] = py
        else:
            parents[py] = px


p, w = map(int, input().split())
c, v = map(int, input().split())

roads = sorted([list(map(int, input().split())) for _ in range(w)], key=lambda x: x[2], reverse=True)

parents = [_ for _ in range(p)]

mn = float('inf')

for i in range(w):
    if find_set(c) == find_set(v):
        break
    if find_set(roads[i][0]) != find_set(roads[i][1]):
        if mn > roads[i][2]:
            mn = roads[i][2]
        union(roads[i][0], roads[i][1])

print(mn)