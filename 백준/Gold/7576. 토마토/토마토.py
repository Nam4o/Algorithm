import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque(first_tomato[:])
    for w in queue:
        visited[w[0]][w[1]] = 1

    while queue:
        n = queue.popleft()

        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = visited[n[0]][n[1]] + 1


M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0
first_tomato = []

for a in range(N):
    for b in range(M):
        if arr[a][b] == 1:
            first_tomato.append([a, b])
        elif arr[a][b] == 0:
            cnt += 1
        else:
            visited[a][b] = -1

bfs()

mx = 1
is_possible = True


for a in range(N):
    if is_possible == False:
        break
    for b in range(M):
        if visited[a][b] == 0:
            is_possible = False
            break

        elif visited[a][b] > mx:
            mx = visited[a][b]


if cnt == 0:
    print(0)
elif is_possible == False:
    print(-1)
elif mx > 1:
    print(mx - 1)