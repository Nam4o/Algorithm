from collections import deque
import sys
input = sys.stdin.readline


def bfs(st):
    global size, time, start, check
    visited = [[0] * N for _ in range(N)]
    di, dj = [-1, 0, 0, 1], [0, -1, 1, 0]
    queue = deque()
    visited[st[0]][st[1]] = 1
    tmp1 = [st[0], st[1], 1]
    queue.append(tmp1)

    stack = []

    while queue:

        n = queue.popleft()

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] <= size:
                visited[ni][nj] = visited[n[0]][n[1]] + 1
                queue.append([ni, nj, visited[ni][nj]])
                if size > arr[ni][nj] and arr[ni][nj] != 0:
                    stack.append([ni, nj,visited[ni][nj]])

    if stack:
        stack.sort(key=lambda x: (x[2], x[0], x[1]))
        start = [stack[0][0], stack[0][1]]
        time += stack[0][2] - 1
        arr[start[0]][start[1]] = 0
        return
    else:
        check = False
        return



N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

many = 0
time = 0
size = 2
start =[]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start = [i, j]
            arr[i][j] = 0
        elif arr[i][j] != 0:
            many += 1
cnt = size
check = True
while many != 0 and check == True:
    bfs(start)
    cnt -= 1
    many -= 1
    if cnt == 0:
        size += 1
        cnt = size
print(time)

