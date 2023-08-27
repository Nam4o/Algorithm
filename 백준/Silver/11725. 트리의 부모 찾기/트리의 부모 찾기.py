import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

def BFS(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        n = queue.popleft()
        for w in connection[n]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1
                par[w] = n

arr = [list(map(int, input().split())) for _ in range(N - 1)]

visited = [0] * (N + 1)
par = deque([0] * (N + 1))

connection = [[] for _ in range(N + 1)]

for i in range(len(arr)):
    connection[arr[i][1]].append(arr[i][0])
    connection[arr[i][0]].append(arr[i][1])

BFS(1)
par.popleft()
par.popleft()
while par:
    print(par.popleft())
