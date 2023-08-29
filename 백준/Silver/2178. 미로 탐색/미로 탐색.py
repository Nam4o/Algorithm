import sys
from collections import deque

input = sys.stdin.readline

def bfs(si, sj):
    queue = deque()
    queue.append([si, sj])
    visited[si][sj] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


    while queue:
        n = queue.popleft()

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = visited[n[0]][n[1]] + 1


    return visited[N - 1][M - 1]


N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

print(bfs(0, 0))