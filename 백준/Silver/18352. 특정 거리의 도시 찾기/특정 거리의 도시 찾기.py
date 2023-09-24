import heapq,sys
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

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

res = dijkstra(graph, X)

if res.count(K) == 0:
    print(-1)
else:
    for i in range(len(res)):
        if res[i] == K:
            print(i)