import sys
input = sys.stdin.readline


def dfs(now):
    global ans

    di, dj = [0, 0, 1, -1], [1, -1, 0, 0]

    if visited[now[0]][now[1]][0] == n:
        ans += visited[now[0]][now[1]][1]
        return

    for k in range(4):
        ni, nj = now[0] + di[k], now[1] + dj[k]
        if visited[ni][nj][0] == -1:
            if k == 0 and east != 0:
                visited[ni][nj] = [visited[now[0]][now[1]][0] + 1, visited[now[0]][now[1]][1] * east]
                dfs([ni, nj])
                visited[ni][nj] = [- 1, visited[now[0]][now[1]][1] // east]
            elif k == 1 and west != 0:
                visited[ni][nj] = [visited[now[0]][now[1]][0] + 1, visited[now[0]][now[1]][1] * west]
                dfs([ni, nj])
                visited[ni][nj] = [- 1, visited[now[0]][now[1]][1] // west]
            elif k == 2 and south != 0:
                visited[ni][nj] = [visited[now[0]][now[1]][0] + 1, visited[now[0]][now[1]][1] * south]
                dfs([ni, nj])
                visited[ni][nj] = [- 1, visited[now[0]][now[1]][1] // south]
            elif k == 3 and north != 0:
                visited[ni][nj] = [visited[now[0]][now[1]][0] + 1, visited[now[0]][now[1]][1] * north]
                dfs([ni, nj])
                visited[ni][nj] = [- 1, visited[now[0]][now[1]][1] // north]






n, east, west, south, north = map(int, input().split())

east, west, south, north = east / 100, west / 100, south / 100, north / 100

arr = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]

visited = [[[-1, 0] for _ in range((2 * n + 1))] for _ in range(2 * n + 1)]
visited[n][n][0] = 0
visited[n][n][1] = 1
start = [n, n]

ans = 0
dfs(start)
print(ans)
