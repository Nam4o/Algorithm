import sys
input = sys.stdin.readline

def dfs(s):
    global cnt
    global numb

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    stack = []
    stack.append(s)
    visited[s[0]][s[1]] = 1

    while stack:
        n = stack.pop()

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and apart[ni][nj] == 1 and visited[ni][nj] == 0:
                stack.append([ni, nj])
                visited[ni][nj] = 1
                cnt += 1
    result.append(cnt)
    numb += 1
    cnt = 1

N = int(input())

apart = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

cnt = 1

numb = 0

result = []

for i in range(N):
    for j in range(N):
        if apart[i][j] == 1 and visited[i][j] == 0:
            dfs([i, j])
print(numb)
result.sort()
for i in result:
    print(i)