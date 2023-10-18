import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    global cmp

    heap = []
    heapq.heappush(heap, (0, start))
    seconds[start] = 0

    while heap:
        current, node = heapq.heappop(heap)

        for next, s in graph[node]:
            new_second = current + s
            if seconds[next] > new_second:
                seconds[next] = new_second
                heapq.heappush(heap, (new_second, next))


    return seconds
T = int(input())

for tc in range(T):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for u in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    seconds = [float('inf')] * (n + 1)

    cmp = 0

    dijkstra(c)

    ans = 0
    for i in range(1, len(seconds)):
        if seconds[i] != float('inf'):
            cmp += 1
            if seconds[i] > ans:
                ans = seconds[i]

    print(cmp, ans)
