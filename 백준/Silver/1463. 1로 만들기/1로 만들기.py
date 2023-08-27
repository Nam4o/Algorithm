import sys
from collections import deque
input = sys.stdin.readline


def DP(X):
    if X == 1:
        return 0
    
    dp = [0] * (X + 1)
    queue = deque()
    queue.append(X)

    while queue:
        s = queue.popleft()

        if s % 3 == 0 and dp[s // 3] == 0:
            queue.append(s // 3)
            dp[s // 3] = dp[s] + 1
        if s % 2 == 0 and dp[s // 2] == 0:
            queue.append(s // 2)
            dp[s // 2] = dp[s] + 1
        if s - 1 >= 1 and dp[s - 1] == 0:
            queue.append(s - 1)
            dp[s - 1] = dp[s] + 1
        if dp[1] != 0:
            return dp[1]

X = int(input())
print(DP(X))