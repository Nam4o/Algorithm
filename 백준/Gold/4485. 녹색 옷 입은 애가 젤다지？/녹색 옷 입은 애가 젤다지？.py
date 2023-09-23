import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    heap = [(arr[start[0]][start[1]], start)]
    cost = [[float('inf')] * N for _ in range(N)]
    cost[start[0]][start[1]] = arr[start[0]][start[1]]

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while heap:
        current, now = heapq.heappop(heap)
        if now == (N - 1, N - 1):
            return cost[now[0]][now[1]]
        for k in range(4):
            ni, nj = now[0] + di[k], now[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                new_cost = current + arr[ni][nj]
                if cost[ni][nj] > new_cost:
                    cost[ni][nj] = new_cost
                    heapq.heappush(heap, (new_cost, (ni, nj)))
                    
                    
tc = 1

while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = (0, 0)
    print(f'Problem {tc}: {dijkstra(start)}')
    tc += 1