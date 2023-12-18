import sys
input = sys.stdin.readline
N = int(input())

cost = [0] + [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 2)]
day = [0 for _ in range(N + 2)]

for i in range(1, N + 1):
    if i + cost[i][0] - 1 <= N:
        dp[i + cost[i][0] - 1] = max(dp[i + cost[i][0] - 1], dp[i - 1] + cost[i][1])
    dp[i] = max(dp[i], dp[i - 1])
print(dp[N])