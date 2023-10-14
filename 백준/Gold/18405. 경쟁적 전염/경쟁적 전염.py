from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):

    queue = deque(start)
    for t in start:
        visited[t[0]][t[1]] = True

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    while queue:
        # queue.sort(key=lambda x: (x[3], x[2]))
        n = queue.popleft()
        if n[3] == S:
            if n[0] == X - 1 and n[1] == Y - 1:
                return n[2]
        elif n[3] < S:
            if arr[X - 1][Y - 1] != 0:
                return arr[X - 1][Y - 1]
        elif n[3] > S:
            return 0

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and arr[ni][nj] == 0:
                visited[ni][nj] = True
                arr[ni][nj] = n[2]
                queue.append([ni, nj, n[2], n[3] + 1])


N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

visited = [[False] * N for _ in range(N)]

start = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            start.append([i, j, arr[i][j], 0])

start.sort(key=lambda x:x[2])


print(bfs(start))