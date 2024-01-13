import heapq, sys
input = sys.stdin.readline

def dijkstra(start, arrive):
    heap = [(0, start)]
    distance = [int(1e9)] * (N + 1)
    distance[start] = 0

    while heap:
        current, node = heapq.heappop(heap)
        for next, d in graph[node]:
            new_dist = current + d
            if distance[next] > new_dist:
                distance[next] = new_dist
                heapq.heappush(heap, (new_dist, next))

    return distance[arrive]

T = int(input())

for tc in range(T):
    # N : 노드 개수, M : 간선 개수, T : 목적지 후보 개수
    N, M, T = map(int, input().split())
    # S : 출발점, G, H : 이미 지난 간선 ( UNION )
    S, G, H = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    cand = sorted([int(input()) for _ in range(T)])

    res = []

    for j in cand:

        if dijkstra(S, G) + dijkstra(H, j) + dijkstra(G, H) == dijkstra(S, j) or dijkstra(S, H) + dijkstra(G, j) + dijkstra(G, H) == dijkstra(S, j):
            res.append(j)
    print(*res)