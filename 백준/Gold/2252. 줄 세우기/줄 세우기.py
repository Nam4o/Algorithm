from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)


for _ in range(M):
    A, B = map(int, input().split())
    in_degree[B] += 1
    graph[A].append(B)
visited = [False] * (N + 1)

deq = deque()

ans = []

i = 0

for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        deq.append(i)
        visited[i] = True

while deq:
    n = deq.popleft()
    ans.append(n)
    for j in graph[n]:
        if visited[j] == False:

            in_degree[j] -= 1
            if in_degree[j] == 0:
                deq.append(j)
                visited[j] = True

print(*ans)
