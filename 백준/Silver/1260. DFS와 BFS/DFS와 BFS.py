from collections import deque
import sys
input = sys.stdin.readline

def dfs(s):

    visited = [0] * (N + 1)
    stack = []
    visited[s] = 1

    ans_dfs.append(s)


    while True:
        for w in range(1, N + 1):
            if w in connection[s] and visited[w] == 0:
                stack.append(s)
                stack.append(w)
                ans_dfs.append(w)
                s = w
                visited[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


def bfs(s):
    visited = [0] * (N + 1)
    queue = deque()
    queue.append(s)


    while queue:
        n = queue.popleft()
        if visited[n] == 0:
            visited[n] = 1
            ans_bfs.append(n)
            connection[n].sort()
            for k in connection[n]:
                queue.append(k)

    return ans_bfs


N, M, V = map(int, input().split())

arr = []
ans_dfs = []
ans_bfs = []

for _ in range(M):
    A, B = map(int, input().split())
    arr.append(A)
    arr.append(B)

connection = [[] for _ in range(N + 1)]

for ar in range(0, len(arr), 2):
    connection[arr[ar]].append(arr[ar + 1])
    connection[arr[ar + 1]].append(arr[ar])
dfs(V)
bfs(V)
print(*ans_dfs)
print(*ans_bfs)