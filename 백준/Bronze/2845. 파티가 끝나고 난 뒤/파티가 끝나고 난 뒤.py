L, P = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(5):
    arr[i] = arr[i] - (L * P)
print(*arr)
