import sys
input = sys.stdin.readline

def prime_numbers(n):

    end = int(n ** (1 / 2))
    for i in range(2, end + 1):
        if arr[i] == 0:
            continue
        for j in range(i * i, n + 1, i):
            arr[j] = 0


M, N = map(int, input().split())

arr = [_ for _ in range(N + 1)]

prime_numbers(N)
for k in range(M, N + 1):
    if arr[k] != 0 and k != 1:
        print(arr[k])
