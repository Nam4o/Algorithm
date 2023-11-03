import sys
input = sys.stdin.readline

def find_set(x):
    if x == parents[x][0]:
        return x
    else:
        parents[x][0] = find_set(parents[x][0])
        return parents[x][0]


def union(x, y):
    px, py = find_set(x), find_set(y)

    if px < py:
        parents[px][0] = py
    else:
        parents[py][0] = px

N, M = map(int, input().split())

gender = list(input().split())

route = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x:x[2])

parents = [0]

for i in range(1, N + 1):
    parents.append([i, gender[i - 1]])


cnt = 1
amount = 0

for i in range(M):
    s, e = route[i][0], route[i][1]
    if cnt == N:
        break
    if find_set(s) != find_set(e) and parents[s][1] != parents[e][1]:
        cnt += 1
        amount += route[i][2]
        union(s, e)
if cnt == N: 
    print(amount)
else:
    print(-1)