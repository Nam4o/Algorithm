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


N, M = map(int, input().split())
fact = list(map(int, input().split()))
parents = [_ for _ in range(N + 1)]
arr = [list(map(int, input().split())) for _ in range(M)]

cnt = 0
if fact[0] != 0:
    for i in arr:
        for j in range(1, i[0] + 1):
            for k in range(j, i[0] + 1):
                union(i[j], i[k])
    for x in arr:
        check = True
        for y in range(1, x[0] + 1):
            for z in range(1, fact[0] + 1):
                if find_set(x[y]) == find_set(fact[z]):
                    check = False
                    break
            if check == False:
                break
        if check:
            cnt += 1
    print(cnt)
else:
    print(M)