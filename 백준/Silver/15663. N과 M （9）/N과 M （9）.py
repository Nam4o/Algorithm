import sys
input = sys.stdin.readline


def comb(depth, current):
    if depth == M:
        for i in result:
            if result.count(i) > base.count(i):
                return
        print(*result)
        return

    for i in range(current, len(arr)):
        result.append(arr[i])
        comb(depth + 1, current)
        result.pop()


N, M = map(int, input().split())

base = list(map(int, input().split()))
arr = set(base)
arr = sorted(list(arr))
result = []
check = [False] * N

comb(0, 0)