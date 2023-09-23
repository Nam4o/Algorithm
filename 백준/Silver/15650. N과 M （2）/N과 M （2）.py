import sys
input = sys.stdin.readline

def comb(arr, depth, current):
    if depth == M:

        print(*ans)
        return

    for i in range(current, len(arr)):
        if check[i]:
            continue
        check[i] = True
        ans.append(arr[i])
        comb(arr, depth + 1, i + 1)
        check[i] = False
        ans.pop()


N, M = map(int, input().split())
arr = [_ for _ in range(1, N + 1)]
check = [False for _ in range(N)]
ans = []
comb(arr, 0, 0)
