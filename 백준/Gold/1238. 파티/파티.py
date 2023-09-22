import heapq, sys
input = sys.stdin.readline

def dijkstra(graph, start):
    heap = [(0, start)]
    distance = [float('inf')] * (N + 1)
    distance[start] = 0

    while heap:
        current, node = heapq.heappop(heap)

        for next, d in graph[node]:
            new_dist = current + d
            if distance[next] > new_dist:
                distance[next] = new_dist
                heapq.heappush(heap, (new_dist, next))

    return distance


N, M, X = map(int, input().split())


graph1 = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph1[a].append((b, c))
    graph2[b].append((a, c))
ans = 0

i = dijkstra(graph1, X)
j = dijkstra(graph2, X)
for k in range(1, len(i)):
    if i[k] + j[k] > ans:
        ans = i[k] + j[k]
print(ans)