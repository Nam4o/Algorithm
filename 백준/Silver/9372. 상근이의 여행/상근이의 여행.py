import sys

input = sys.stdin.readline

T = int(input())

def dfs(s):
    stack = []
    visited[s] = 1
    cnt = 0
    while True:
        for w in range(1, N + 1):
            if connect[s][w] == 1 and visited[w] == 0:
                stack.append(s)
                s = w
                visited[s] = 1
                cnt += 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    return cnt


for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(M)]

    connect = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for i in range(len(arr)):
        connect[arr[i][0]][arr[i][1]] = 1
        connect[arr[i][1]][arr[i][0]] = 1

    print(dfs(1))
