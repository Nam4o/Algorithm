import sys
input = sys.stdin.readline


def comb(depth, current):
    if depth == M:
        for i in range(1, len(result)):
            if result[i] < result[i - 1]:
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