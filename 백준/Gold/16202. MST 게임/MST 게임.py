import sys
input = sys.stdin.readline


def find_set(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find_set(parents[x])
        return parents[x]


def union(x, y):
    px, py = find_set(x), find_set(y)
    if px != py:
        if px < py:
            parents[px] = py
        else:
            parents[py] = px


N, M, K = map(int, input().split())

arr = []



for w in range(1, M + 1):
    a, b = map(int, input().split())
    arr.append([a, b, w])

ans = []

for i in range(K):
    parents = [_ for _ in range(N + 1)]
    cnt, amount = 0, 0
    for j in range(i, M):
        if cnt == N:
            ans.append(amount)
            break
        if find_set(arr[j][0]) != find_set(arr[j][1]):
            cnt += 1
            amount += arr[j][2]
            union(arr[j][0], arr[j][1])

    if cnt == N - 1:
        ans.append(amount)
    elif cnt < N - 1:
        ans.append(0)

print(*ans)

