import sys
input = sys.stdin.readline

K = int(input())

arr = list(map(int, input().split()))

stairs = [[] for _ in range(K)]


for j in range(K):
    for i in range((2 ** (K - j) - 1 ) // 2, len(arr), 2 ** (K - j)):
        stairs[j].append(arr[i])

for k in stairs:
    print(*k)