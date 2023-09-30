import sys
input = sys.stdin.readline

def bellman(start):
    time = [float('inf')] * (N + 1)
    time[start] = 0

    for i in range(N):
        for node, next, t in arr:
            new_time = time[node] + t
            if time[node] != float('inf') and time[next] > new_time:
                time[next] = new_time
                if i == N - 1:
                    return -1
    
    return time


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

res = bellman(1)


if res == -1:
    print(-1)
else:
    for j in range(2, N + 1):
        if res[j] == float('inf'):
            print(-1)
        else:
            print(res[j])