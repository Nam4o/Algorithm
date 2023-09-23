import sys
input = sys.stdin.readline

def comb(arr, depth, current):
    if depth == M:
        for k in range(1, len(ans)):
            if ans[k] < ans[k - 1]:
                return
        print(*ans)
        return

    for i in range(current, len(arr)):
        ans.append(arr[i])
        comb(arr, depth + 1, current)
        check[i] = False
        ans.pop()


N, M = map(int, input().split())
arr = [_ for _ in range(1, N + 1)]
check = [False for _ in range(N)]
ans = []
comb(arr, 0, 0)
