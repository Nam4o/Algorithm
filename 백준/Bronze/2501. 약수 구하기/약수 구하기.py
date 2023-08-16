N, K = map(int, input().split())

result = []

for i in range(1,N + 1):
    if N % i == 0:
        result.append(i)
if len(result) >= K:
    print(result[K - 1])
else:
    print(0)