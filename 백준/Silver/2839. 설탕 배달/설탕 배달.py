N = int(input())
def find(N):
    dp = [0] * (N + 1)
    queue = []
    queue.append(N)

    while queue:
        s = queue.pop(0)
        if dp[0] != 0:
            return dp[0]
        a = s - 3
        b = s - 5
        if a >= 0 and dp[a] == 0:
            queue.append(a)
            dp[a] = dp[s] + 1
        if b >= 0 and dp[b] == 0:
            queue.append(b)
            dp[b] = dp[s] + 1
    return -1

print(find(N))