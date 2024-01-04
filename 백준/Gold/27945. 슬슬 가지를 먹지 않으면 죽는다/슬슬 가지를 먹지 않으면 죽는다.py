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



n, m = map(int, input().split())

arr = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])
day = 1
parents = [_ for _ in range(n + 1)]

for i in range(m):
    if day == n:
        break
    if find_set(arr[i][0]) != find_set(arr[i][1]):
        if arr[i][2] == day:
          
            day += 1
            union(arr[i][0], arr[i][1])
        else:

            break


print(day)