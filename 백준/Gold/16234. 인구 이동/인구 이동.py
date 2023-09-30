from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    global cnt
    global check

    queue = deque([start])
    tmp_cnt = 1
    population = arr[start[0]][start[1]]
    visited[start[0]][start[1]] = cnt + 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.popleft()
        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if L <= abs(arr[n[0]][n[1]] - arr[ni][nj]) <= R:
                    visited[ni][nj] = cnt + 1
                    population += arr[ni][nj]
                    tmp_cnt += 1
                    queue.append([ni, nj])
    cnt += 1

    def change(start):
        queue_change = deque([start])
        new = population // tmp_cnt
        arr[start[0]][start[1]] = new
        tmp_visited = [[False] * N for _ in range(N)]
        tmp_visited[start[0]][start[1]] = True

        while queue_change:
            t = queue_change.popleft()
            for k in range(4):
                ni, nj = t[0] + di[k], t[1] + dj[k]
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == cnt and tmp_visited[ni][nj] == False:
                    tmp_visited[ni][nj] = True
                    arr[ni][nj] = new
                    queue_change.append([ni, nj])

    if tmp_cnt > 1:
        change(start)
        check += 1

N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


ans = 0

while True:
    visited = [[0] * N for _ in range(N)]
    check = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs([i, j])
    if check == 0:
        break
    else:
        ans += 1

print(ans)