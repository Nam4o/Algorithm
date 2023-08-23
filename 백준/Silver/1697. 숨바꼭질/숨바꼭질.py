import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

# 걸을 땐 현재 위치 + - 1
# 순간이동 할 땐 현재 위치 * 2

dp = [0]*100001

def minus(x):
    nx = x - 1
    if 0 <= nx <= 100000 and dp[nx] == 0:
        dp[nx] = dp[x] + 1

    return nx

def plus(x):
    nx = x + 1
    if 0 <= nx <= 100000 and dp[nx] == 0:
        dp[nx] = dp[x] + 1
    return nx

def teleport(x):
    nx = x * 2
    if 0 <= nx <= 100000 and dp[nx] == 0:
        dp[nx] = dp[x] + 1
    return nx

queue = deque([])
queue.append(N)
dp[N]= 0

while queue:
    if K in queue:
        break

    t = queue.popleft()
    if 0 <= t - 1 <= 100000 and dp[t - 1] == 0 and minus(t) not in queue:
        queue.append(minus(t))
    if t + 1 <= 100000 and dp[t + 1] == 0 and plus(t) not in queue:
        queue.append(plus(t))
    if t * 2 <= 100000 and dp[t * 2] == 0 and teleport(t) not in queue:
        queue.append(teleport(t))

print(dp[K])