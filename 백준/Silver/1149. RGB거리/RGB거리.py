import sys
input = sys.stdin.readline

N = int(input().strip())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[] * N for _ in range(N)]

for _ in range(3):
    dp[0].append(arr[0][_])

for i in range(1, len(arr)):
    for j in range(3):
        inner = []
        for k in range(3):
            if k != j:
                inner.append(arr[i][j] + dp[i - 1][k])
        dp[i].append(min(inner))

print(min(dp[-1]))