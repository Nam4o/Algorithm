import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
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


# N : 정점 개수, M : 수색 범위, R : 간선 개수
N, M, R = map(int, input().split())
# N : 각 정점에 있는 아이템 수
T = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

mx = 0

for i in range(1, N + 1):
    inner = 0
    tmp = dijkstra(i)
    for j in range(1, N + 1):
        if tmp[j] <= M:
            inner += T[j]
    if inner > mx:
        mx = inner
print(mx)