import heapq, sys
input = sys.stdin.readline


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start, start))

    cost = [float('inf')] * (N + 1)
    cost[start] = 0
    ans = [0] * (N + 1)
    ans[start] = '-'
    while heap:
        current, node, first = heapq.heappop(heap)


        for next, c in graph[node]:
            new_cost = current + c
            if cost[next] > new_cost:
                cost[next] = new_cost
                if node == start:
                    first = next
                    ans[next] = first

                    heapq.heappush(heap, (new_cost, next, first))
                else:
                    ans[next] = first
                    heapq.heappush(heap, (new_cost, next, first))
    return ans[1:]




N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, N + 1):
    print(*dijkstra(i))