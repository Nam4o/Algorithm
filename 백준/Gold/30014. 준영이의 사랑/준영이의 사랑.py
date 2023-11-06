from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

arr = deque(sorted(list(map(int, input().split()))))


amount = 0


ans = deque()

ans.append(arr.popleft())
while arr:
    if len(ans) == 1:
        ans.append(arr.popleft())
    else:
        tmp = arr.popleft()
        if abs(ans[0] - tmp) > abs(ans[-1] - tmp):
            ans.appendleft(tmp)
        else:
            ans.append(tmp)


for i in range(1, N):
    amount += ans[i - 1] * ans[i]

amount += ans[0] * ans[-1]


print(amount)
print(*ans)