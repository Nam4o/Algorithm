import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque(first_tomato[:])
    for w in queue:
        visited[w[0]][w[1]][w[2]] = 1

    while queue:
        n = queue.popleft()

        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
        for k in range(4):
            ni, nj = n[1] + di[k], n[2] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[n[0]][ni][nj] == 0 and visited[n[0]][ni][nj] == 0:
                queue.append([n[0], ni, nj])
                visited[n[0]][ni][nj] = visited[n[0]][n[1]][n[2]] + 1

        if H >= 2:
            if 0 <= n[0] - 1 < H and arr[n[0] - 1][n[1]][n[2]] == 0 and visited[n[0] - 1][n[1]][n[2]] == 0:
                visited[n[0] - 1][n[1]][n[2]] = visited[n[0]][n[1]][n[2]] + 1
                queue.append([n[0] - 1, n[1], n[2]])

            if 0 <= n[0] + 1 < H and arr[n[0] + 1][n[1]][n[2]] == 0 and visited[n[0] + 1][n[1]][n[2]] == 0:
                visited[n[0] + 1][n[1]][n[2]] = visited[n[0]][n[1]][n[2]] + 1
                queue.append([n[0] + 1, n[1], n[2]])

    return

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

cnt = 0
first_tomato = []
for a in range(H):
    for b in range(N):
        for c in range(M):
            if arr[a][b][c] == 1:
                first_tomato.append([a, b, c])
            elif arr[a][b][c] == 0:
                cnt += 1
            else:
                visited[a][b][c] = -1

bfs()

mx = 1
is_possible = True

for a in range(H):
    if is_possible == False:
        break
    for b in range(N):
        if is_possible == False:
            break
        for c in range(M):
            if visited[a][b][c] == 0:
                is_possible = False
                break

            elif visited[a][b][c] > mx:
                mx = visited[a][b][c]

if cnt == 0:
    print(0)
elif is_possible == False:
    print(-1)
elif mx > 1:
    print(mx - 1)