from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global check

    deq = deque()
    deq.append(start)
    visited[start[0]][start[1]] = True
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while deq:
        n = deq.popleft()
        if n[0] == M - 1 and arr[n[0]][n[1]] == 0:
            check = True
            return
        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == False and arr[ni][nj] == 0:
                deq.append([ni, nj])
                visited[ni][nj] = True


M, N = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

check = False

for i in range(0, 1):
    for j in range(N):
        if arr[i][j] == 0 and visited[i][j] == False and check == False:
            bfs([i, j])

if check:
    print("YES")
else:
    print("NO")

