import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    heap = [(0, start)]

    cost = [float('inf')] * (N + 1)
    cost[start] = 0

    while heap:
        current, node = heapq.heappop(heap)

        for next, c in graph[node]:
            new_cost = current + c
            if cost[next] > new_cost:
                cost[next] = new_cost
                heapq.heappush(heap, (new_cost, next))
    return cost


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for i in range(M):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])
        graph[e].append([s, w])

    K = int(input())
    room = list(map(int, input().split()))

    mn = float('inf')

    ans = 0

    for i in range(1, N + 1):
        tmp = dijkstra(i)
        amount = 0
        for j in room:
            amount += tmp[j]
        if amount < mn:
            mn = amount
            ans = i
    print(ans)