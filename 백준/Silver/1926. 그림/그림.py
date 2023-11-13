from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global mx, paint_cnt
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    cnt = 1

    while queue:
        n = queue.popleft()
        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                queue.append([ni, nj])
                visited[ni][nj] = 1
                cnt += 1
    if cnt != 0:
        paint_cnt += 1
    if cnt > mx:
        mx = cnt


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

mx = 0

paint_cnt = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j]:
            bfs([i, j])

print(paint_cnt)
print(mx)
