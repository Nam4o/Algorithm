import heapq, sys
input = sys.stdin.readline


def dijkstra(start):
    global cnt
    cost = [float('inf')] * (N + 1)
    heap = [(0, start)]

    cost[start] = 0

    while heap:
        current, node = heapq.heappop(heap)
        if cost[node] < current:
            continue

        for next, c in graph[node]:
            next_cost = current + c
            if cost[next] > next_cost:
                cost[next] = next_cost
                heapq.heappush(heap, (next_cost, next))
                dp[next] = node

    return cost

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
ans = []
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, destination = map(int, input().split())
check = destination

dp = [0] * (N + 1)


res = dijkstra(start)
while check != start:
    ans.append(check)
    check = dp[check]
ans.append(start)
ans.reverse()


print(res[destination])
print(len(ans))
print(*ans)

