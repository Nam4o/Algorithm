def bfs(s):
    global mx
    global visited

    if arr[s[0]][s[1]] == 1:
        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
        queue = []
        queue.append(s)
        cnt = 1

        while queue:

            n = queue.pop(0)
            for k in range(4):
                ni, nj = n[0] + di[k], n[1] + dj[k]
                if 0 <= ni < N and 0 <= nj <M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    cnt += 1
                    queue.append((ni, nj))
    return cnt
N, M, K = map(int, input().split())

trashs = [list(map(int, input().split())) for _ in range(K)]
visited = [[0] * M for _ in range(N)]

arr = [[0] * M for _ in range(N)]
mx = 0

tmp = []
for trash in range(len(trashs)):
    arr[trashs[trash][0] - 1][trashs[trash][1] - 1] = 1

result = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            s = (i, j)
            visited[s[0]][s[1]] = 1
            result.append(bfs(s))

print(max(result))
