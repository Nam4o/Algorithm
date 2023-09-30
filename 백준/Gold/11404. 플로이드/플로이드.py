import sys
input = sys.stdin.readline

def floyd():
    cost = [[float('inf')] * N for _ in range(N)]

    for _ in range(N):
        cost[_][_] = 0

    for node in range(1, N + 1):
        for next, c in graph[node]:
            if cost[node - 1][next - 1] > c:
                cost[node - 1][next - 1] = c


    for a in range(N):
        for b in range(N):
            for c in range(N):
                if cost[b][c] > cost[b][a] + cost[a][c]:
                    cost[b][c] = cost[b][a] + cost[a][c]

    return cost

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

res = floyd()

for q in range(N):
    for p in range(N):
        if res[q][p] == float('inf'):
            res[q][p] = 0
    print(*res[q])
