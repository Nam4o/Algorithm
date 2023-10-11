import sys
from collections import  deque
input = sys.stdin.readline

def bfs(start):
    visited = [0] * (N + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        node = queue.popleft()
        for next in relationship[node]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = visited[node] + 1

    return visited

N = int(input())

relationship = [[] for _ in range(N + 1)]

mn_depth = float('inf')

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    relationship[a].append(b)
    relationship[b].append(a)

res = [0] * (N + 1)
for i in range(1, N + 1):
    tmp = max(bfs(i))
    if tmp < mn_depth:
        mn_depth = tmp
    res[i] = tmp

ans = []
cnt = 0
for i in range(1, N + 1):
    if res[i] == mn_depth:
        ans.append(i)
        cnt += 1

print(mn_depth - 1, cnt)
print(*ans)