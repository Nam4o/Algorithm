import heapq, sys
input = sys.stdin.readline

def dijkstra(graph, start):

    heap = [(0, start)]
    distance = [float('inf')] * (V + 1)
    distance[start] = 0

    while heap:
        current, node = heapq.heappop(heap)

        for next, d in graph[node]:
            new_dist = current + d
            if distance[next] > new_dist:
                distance[next] = new_dist
                heapq.heappush(heap, (new_dist, next))
    return distance


V, E = map(int, input().split())
# K : 시작 정점 번호
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

ans = dijkstra(graph, K)

for i in range(1, len(ans)):
    if ans[i] == float('inf'):
        print('INF')
    else:
        print(ans[i])