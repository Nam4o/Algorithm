N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

dp = []
for i in range(1, N + 1):
    dp.append([0] * i)

for x in range(0, N):
    if x == 0:
        dp[x][0] = triangle[x][0]
    elif x == 1:
        dp[x][0] = dp[x - 1][0] + triangle[x][0]
        dp[x][-1] = dp[x - 1][0] + triangle[x][-1]
    for t in range(1, len(dp[x]) - 1):
        if len(dp[x]) > 1:
            dp[x][0] = dp[x - 1][0] + triangle[x][0]
            dp[x][-1] = dp[x - 1][-1] + triangle[x][-1]
            dp[x][t] = max(dp[x - 1][t - 1], dp[x - 1][t]) + triangle[x][t]

print(max(dp[-1]))