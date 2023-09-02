import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

def bfsW(s):

    queue = deque()
    queue.append(s)
    visited[s[0]][s[1]] = 1
    cnt_w = 1
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.popleft()

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 'W' and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1
                cnt_w += 1

    return cnt_w ** 2


def bfsB(s):
    queue = deque()
    queue.append(s)
    visited[s[0]][s[1]] = 1
    cnt_b = 1
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.popleft()

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 'B' and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1
                cnt_b += 1

    return cnt_b ** 2

arr = [list(input().strip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
cnt_w = 0
cnt_b = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and arr[i][j] == 'W':
            cnt_w += bfsW([i, j])
        elif visited[i][j] == 0 and arr[i][j] == 'B':
            cnt_b += bfsB([i, j])
print(cnt_w, cnt_b)

