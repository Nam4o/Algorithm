import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(s):
    visited[s] = 1

    for u in connect[s]:
        if visited[u] == 1:
            continue
            
        dfs(u)
        
    return 1

arr = [list(map(int, input().split())) for _ in range(M)]

visited = [0] * (N + 1)

connect = [[] for _ in range(N + 1)]
for i in range(M):
    connect[arr[i][0]].append(arr[i][1])
    connect[arr[i][1]].append(arr[i][0])

cnt = 0

for t in range(1, N + 1):
    if visited[t] == 0:
        cnt += dfs(t)
print(cnt)