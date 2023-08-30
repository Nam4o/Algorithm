N = int(input())
arr = list(map(int, input().split()))

prime = []
cnt = 0

for i in range(2, max(arr) + 1):
    for j in range(2, i + 1):
        if i == j:
            prime.append(i)
        if i % j == 0:
            break

for k in arr:
    if k in prime:
        cnt += 1

print(cnt)