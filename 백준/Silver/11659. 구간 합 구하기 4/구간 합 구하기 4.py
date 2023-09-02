import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * N
dp[0] = arr[0]

for t in range(N - 1):
    dp[t + 1] = dp[t] + arr[t + 1]

for _ in range(M):
    s, e = map(int, input().split())
    if s - 2 >= 0:
        print(dp[e - 1] - dp[s - 2])
    else:
        print(dp[e - 1])