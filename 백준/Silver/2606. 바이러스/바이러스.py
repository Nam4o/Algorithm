
def dfs(n, V, adj_m):
    global visited
    global result

    stack = []
    visited[n] = True
    while True:
        for w in range(1, V + 1):
            if adj_m[n][w] == 1 and visited[w] == False:
                stack.append(n)
                n = w
                result.append(n)
                visited[n] = True
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return


computers = int(input())

pairs = int(input())

connect = []
visited = [False] * (computers + 1)

for pair in range(pairs):
    connect.append(list(map(int, input().split())))

adj = [[0] * (computers + 1) for _ in range(computers + 1)]
for i in range(pairs):
    v1, v2 = connect[i][0], connect[i][1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1

result = []

dfs(1, computers, adj)

print(len(result))