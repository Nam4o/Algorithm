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
            cnt[py] += cnt[px]
        else:
            parents[py] = px
            cnt[px] += cnt[py]


T = int(input())

for tc in range(1, T + 1):
    parents = {}
    cnt = {}

    F = int(input())
    for _ in range(F):
        p1, p2 = input().split()
        if p1 not in parents:
            parents[p1] = p1
            cnt[p1] = 1
        if p2 not in parents:
            parents[p2] = p2
            cnt[p2] = 1
        union(p1, p2)

        print(cnt[find_set(p1)])
