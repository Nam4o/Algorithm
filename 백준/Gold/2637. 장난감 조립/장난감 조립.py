from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# X, Y, K 세 부품, 중간 부품이나 완제품 X 를 만드는데
# 중간 부품 혹은 기본 부품 Y 가 K 개 필요하다.


in_degree = [0] * (N + 1)

dp = [[0] * (N + 1) for _ in range(N + 1)]

leaf = [0] * (N + 1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    in_degree[Y] += 1
    dp[X][Y] = K
    leaf[X] += 1


memo = [0] * (N + 1)

queue = deque()


for i in range(1, N + 1):
    if not in_degree[i]:
        queue.append(i)
        memo[i] = 1


while queue:
    n = queue.popleft()
    for next in range(1, N + 1):
        if dp[n][next] == 0:
            continue
        if in_degree[next] > 0:
            in_degree[next] -= 1
            memo[next] += memo[n] * dp[n][next]
            dp[n][next] = 0
        else:
            continue
        if in_degree[next] == 0:
            queue.append(next)
        else:
            queue.append(n)



for r in range(1, N + 1):
    if leaf[r] == 0:
        print(r, memo[r])
