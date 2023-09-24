import heapq, sys
input = sys.stdin.readline

def dijkstra(graph, start):
    heap = [(0, start)]
    cost = [float('inf')] * (N + 1)
    cost[start] = 0

    while heap:
        current, node = heapq.heappop(heap)
        if current >= cost[e]:
            break
        for next, c in graph[node]:
            new_cost = current + c
            if cost[next] > new_cost:
                cost[next] = new_cost
                heapq.heappush(heap, (new_cost, next))
    return cost[e]


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())

print(dijkstra(graph, s))