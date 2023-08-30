N, M = map(int, input().split())
arr = [input() for _ in range(N)]
result = []
red = 0
blue = 0
white = 0
for i in range(0, N - 2):
    white += (M - arr[i].count('W'))
    for j in range(i + 1, N - 1):
        blue += (M - arr[j].count('B'))
        for k in range(j + 1, N):
            red += (M - arr[k].count('R'))
        result.append(white + blue + red)
        red = 0
    blue = 0
print(min(result))