T = int(input())


def DFS():
    global cnt

    queue = []
    i, j = 0, 0

    while i < N and j < M:
        if field[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            queue.append((i, j))
            while queue:
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 1 and visited[ni][nj] == False:
                        visited[ni][nj] = True
                        queue.append((ni, nj))
                else:
                    queue.pop(0)
                if queue:
                    i, j = queue[0]
                else:
                    cnt += 1
                    i = 0
                    j = 0
        j += 1
        if j == M:
            i += 1
            j = 0
    return cnt


for tc in range(T):
    # M : 배추밭의 가로길이
    # N : 배추밭의 세로길이
    # K : 배추의 위치의 개수
    M, N, K = map(int, input().split())

    field = [[0] * (M + 1) for _ in range(N + 1)]
    visited = [[False] * (M + 1) for _ in range(N + 1)]

    for _ in range(K):
        # X, Y : 배추의 위치 ( 이차원 리스트 좌표 형식 )
        X, Y = map(int, input().split())
        field[Y][X] = 1

    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]


    cnt = 0

    print(DFS())