import sys
input = sys.stdin.readline

def comb(arr, depth, current):

    if depth == M:
        print(*result)
        return

    for i in range(current, len(arr)):
        if check[i]:
            continue
        check[i] = True
        result.append(arr[i])
        comb(arr, depth + 1, current)
        check[i] = False
        result.pop()




N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))
result = []
check = [False] * N

comb(arr, 0, 0)