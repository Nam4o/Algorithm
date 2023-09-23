import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    heap = [(0, start)]
    weight = [float('inf')] * (N + 1)
    weight[start] = 0

    while heap:
        current, node = heapq.heappop(heap)

        for next, w in graph[node]:
            new_weight = current + w
            if weight[next] > new_weight:
                weight[next] = new_weight
                heapq.heappush(heap, (new_weight, next))

    return weight

def way(x, y):
    base = dijkstra(1)
    first = dijkstra(x)
    second = dijkstra(y)

    return base[x] + first[y] + second[N]


N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

parents = [_ for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

x, y = map(int, input().split())
ans = min((way(x, y), way(y, x)))

if ans == float('inf'):
    print(-1)
else:
    print(ans)
