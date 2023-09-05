import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

def bfs(s):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append(s)
    visited[s[0]][s[1]] = 1

    di, dj = [0, 1, 0, -1, 1, 1, -1, -1], [1, 0, -1, 0, 1, -1, 1, -1]

    while queue:
        n = queue.popleft()
        for k in range(8):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                visited[ni][nj] = visited[n[0]][n[1]] + 1
                queue.append([ni, nj])
            elif 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                result.append(visited[n[0]][n[1]])
                queue.clear()
                break


arr = [list(map(int, input().split())) for _ in range(N)]
result = []

a, b = 0, 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            bfs([y, x])

print(max(result))