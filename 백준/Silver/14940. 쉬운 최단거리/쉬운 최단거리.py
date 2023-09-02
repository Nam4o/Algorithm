import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
def bfs(i, j):

    queue = deque()
    queue.append([i, j])
    visited[i][j] = 0
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    while queue:
        t = queue.popleft()
        for k in range(4):
            ni, nj = t[0] + di[k], t[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                queue.append([ni, nj])
                visited[ni][nj] = visited[t[0]][t[1]] + 1


arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            si, sj = i, j

bfs(si, sj)
for q in range(N):
    for p in range(M):
        if arr[q][p] == 1 and visited[q][p] == 0:
            visited[q][p] = -1
for _ in range(N):
    print(*visited[_])
