from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

result = {}


ans = []
for i in range(N + M):
    a = input().strip()
    if a not in result:
        result[a] = 1
    else:
        result[a] += 1
    if result[a] == 2:
        ans.append(a)

ans.sort()
ans = deque(ans)

print(len(ans))
while ans:
    print(ans.popleft())