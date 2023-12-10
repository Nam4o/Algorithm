mx = 0

def solution(land):
    global mx
    
    col = 4
    row = len(land)
    
    dp = [[] * 4 for _ in range(row)]
    
    for w in range(4):
        dp[0].append(land[0][w])
    
    for i in range(1, row):
        for j in range(4):
            inner = []
            for k in range(4):
                if j != k:
                    inner.append(land[i][j] + dp[i - 1][k])
            dp[i].append(max(inner))
    
    return max(dp[-1])