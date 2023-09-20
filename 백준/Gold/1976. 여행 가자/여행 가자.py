import sys
input = sys.stdin.readline

def find_set(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x])
        return parent[x]


def union(x, y):
    px, py = find_set(x), find_set(y)

    if px != py:
        parent[px] = py


N = int(input())
M = int(input())

connect = [list(map(int, input().split())) for _ in range(N)]

plan = list(map(int, input().split()))

parent = [_ for _ in range(N + 1)]

for i in range(N):
    for j in range(i, N):
        if connect[i][j] == 1:
            union(i + 1, j + 1)


check = True

a = plan[0]
for k in range(1, len(plan)):
    if find_set(a) != find_set(plan[k]):
        check = False

if check:
    print('YES')
else:
    print('NO')