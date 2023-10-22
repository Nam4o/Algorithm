import sys
input = sys.stdin.readline


def prime(n):
    end = int(n ** (1 / 2))
    for i in range(2, end + 1):
        if arr[i] == 0:
            continue

        for j in range(i * i, n + 1, i):
            arr[j] = 0


N = int(input())

arr = [_ for _ in range(N + 1)]
cnt = 0
ans = []

prime(N)

for t in arr:
    if t != 0 and t != 1:
        ans.append(t)

for i in range(len(ans)):
    amount = ans[i]
    if amount == N:
        cnt += 1
        break
    elif amount > N:
        break
    for j in range(i + 1, len(ans)):
        amount += ans[j]
        if amount == N:
            cnt += 1
            break
        elif amount > N:
            break
print(cnt)
