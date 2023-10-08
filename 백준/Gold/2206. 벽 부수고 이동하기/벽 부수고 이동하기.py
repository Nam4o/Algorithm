import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    queue = deque()
    queue.append(s)
    visited = [[[0] * 2 for _ in range(M)]  for _ in range(N)]
    visited[s[0]][s[1]][s[2]] = 1


    while queue:
        n = queue.popleft()

        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj][n[2]] == 0 and maze[ni][nj] == 0:
                    queue.append([ni, nj, n[2]])
                    visited[ni][nj][n[2]] = visited[n[0]][n[1]][n[2]] + 1
                elif maze[ni][nj] == 1:
                    if n[2] == 0:
                        queue.append([ni, nj, n[2] + 1])
                        visited[ni][nj][n[2] + 1] = visited[n[0]][n[1]][n[2]] + 1

    return visited


N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

ans = bfs([0, 0, 0])
if ans[N - 1][M - 1][0] == 0 and ans[N - 1][M - 1][1] == 0:
    print(-1)
elif ans[N - 1][M - 1][0] == 0:
    print(ans[N - 1][M - 1][1])
elif ans[N - 1][M - 1][1] == 0:
    print(ans[N - 1][M - 1][0])
else:
    print(min(ans[N - 1][M - 1][0], ans[N - 1][M - 1][1]))
