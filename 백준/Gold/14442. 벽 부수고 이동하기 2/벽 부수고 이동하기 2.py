import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    queue = deque()
    queue.append(s)
    visited = [[[0] * (K + 1) for _ in range(M)]  for _ in range(N)]
    visited[s[0]][s[1]][K] = 1


    while queue:
        n = queue.popleft()

        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

        if n[0] == N - 1 and n[1] == M - 1:
            return visited[n[0]][n[1]][n[2]]


        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M :
                if maze[ni][nj] == 0 and visited[ni][nj][n[2]] == 0:
                    queue.append([ni, nj, n[2]])
                    visited[ni][nj][n[2]] = visited[n[0]][n[1]][n[2]] + 1
                elif maze[ni][nj] == 1 and visited[ni][nj][n[2] - 1] == 0:
                    if n[2] > 0:
                        queue.append([ni, nj, n[2] - 1])
                        visited[ni][nj][n[2] - 1] = visited[n[0]][n[1]][n[2]] + 1

    return -1


N, M, K = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]


print(bfs([0, 0, K]))

