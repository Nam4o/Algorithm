import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0] * N for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    dp[i][0] = tmp[0]
    for j in range(1, len(tmp)):
        dp[i][j] = dp[i][j - 1] + tmp[j]


find = [list(map(int, input().split())) for _ in range(M)]

for x1, y1, x2, y2 in find:
    inner_sum = 0
    for t in range(x1 - 1, x2):
        if y1 >= 2:
            inner_sum += dp[t][y2 - 1] - dp[t][y1 - 2]
        else:
            inner_sum += dp[t][y2 - 1]
    print(inner_sum)
