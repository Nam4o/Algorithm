import heapq, sys
input = sys.stdin.readline


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    cost = [float('inf')] * (N + 1)
    cost[start] = 0

    while heap:
        current, node = heapq.heappop(heap)
        for next, c in graph[node]:
            new_cost = current + c
            if cost[next] > new_cost:
                cost[next] = new_cost
                heapq.heappush(heap, [new_cost, next])

    return cost[t]

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

s, t = map(int, input().split())

print(dijkstra(s))