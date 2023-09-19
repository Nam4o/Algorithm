import sys
input = sys.stdin.readline


N = int(input())

def bfs_red(s):
    global cnt_red
    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.pop(0)

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'R' and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1

    cnt_red += 1


def bfs_green(s):
    global cnt_green
    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.pop(0)

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'G' and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1

    cnt_green += 1


def bfs_blue(s):
    global cnt_blue
    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.pop(0)

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'B' and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1
    cnt_blue += 1



def bfs_abnormal(s):
    global cnt_abnormal

    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.pop(0)

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] == 'R' or arr[ni][nj] == 'G':
                    queue.append([ni, nj])
                    visited[ni][nj] = 1

    cnt_abnormal += 1


arr = [input().strip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt_abnormal = 0

cnt_red = 0
cnt_green = 0
cnt_blue = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if arr[i][j] == 'R':
                bfs_red([i, j])

            elif arr[i][j] == 'G':
                bfs_green([i, j])
            elif arr[i][j] == 'B':
                bfs_blue([i, j])

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if arr[i][j] == 'R' or arr[i][j] == 'G':
                bfs_abnormal([i, j])


print((cnt_red + cnt_green + cnt_blue), ( cnt_abnormal + cnt_blue))
