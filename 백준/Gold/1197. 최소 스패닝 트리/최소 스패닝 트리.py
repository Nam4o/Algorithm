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
            parents[py] = px
        else:
            parents[px] = py


def kruskal(start):
    cnt = 0
    res = 0
    for a, b, c in arr:
        if find_set(a) != find_set(b):
            if cnt == V:
                break
    
            union(a, b)
            res += c
            cnt += 1

    return res
V, E = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(E)]

arr.sort(key=lambda x: x[2])

parents = [i for i in range(V + 1)]

print(kruskal(1))