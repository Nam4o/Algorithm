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

# graph = [[] for _ in range(N + 1)]
# for _ in range(M):
#     A, B, C = map(int, input().split())
#     graph[A].append((B, C))
#     graph[B].append((A, C))

arr = [list(map(int, input().split())) for _ in range(M)]


parents = [_ for _ in range(N + 1)]

arr.sort(key=lambda x: x[2])

cnt = 1
amount = 0
for a, b, c, in arr:
    if cnt == N - 1:
        break
    if find_set(a) != find_set(b):
        cnt += 1
        union(a, b)
        amount += c
print(amount)