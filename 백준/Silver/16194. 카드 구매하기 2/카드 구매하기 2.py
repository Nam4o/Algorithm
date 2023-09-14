import sys
input = sys.stdin.readline

N = int(input())

arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = arr[i]
    for j in range(1, i):
        tmp = dp[j] + arr[i - j]
        if tmp < dp[i]:
            dp[i] = tmp
print(dp[N])