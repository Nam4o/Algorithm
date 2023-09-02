import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

result = [0] * N


stack = [[arr[-1], -1]]

for i in range(2, N + 1):
    if arr[-i] > stack[-1][0]:
        while stack != [] and arr[-i] > stack[-1][0]:
            a, b = stack.pop()
            result[b] = N - i + 1
        stack.append([arr[-i], -i])
    else:
        stack.append([arr[-i], -i])
print(*result)