from collections import deque
import sys
input = sys.stdin.readline

def bfs(sheep):
    global cnt

    queue = deque()
    queue.append(sheep)
    visited[sheep[0]][sheep[1]] = True

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


    while queue:
        n = queue.popleft()

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == '#' and visited[ni][nj] == False:
                queue.append([ni, nj])
                visited[ni][nj] = True

    cnt += 1



T = int(input())

for tc in range(T):
    H, W = map(int, input().split())

    arr = [list(input().strip()) for _ in range(H)]

    visited = [[False] * W for _ in range(H)]

    cnt = 0

    for x in range(H):
        for y in range(W):
            if visited[x][y] == False and arr[x][y] == '#':
                bfs([x, y])

    print(cnt)