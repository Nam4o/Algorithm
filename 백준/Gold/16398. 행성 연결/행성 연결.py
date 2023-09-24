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


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
graph = []
parents = [_ for _ in range(N)]

for i in range(N):
    for j in range(i, N):
        if i != j:
            graph.append([i, j, arr[i][j]])

graph.sort(key=lambda x: x[2])

cnt = 0
sum_cost = 0

for j in range(len(graph)):
    if cnt == N:
        break
    if find_set(graph[j][0]) != find_set(graph[j][1]):
        cnt += 1
        sum_cost += graph[j][2]
        union(graph[j][0], graph[j][1])

print(sum_cost)
