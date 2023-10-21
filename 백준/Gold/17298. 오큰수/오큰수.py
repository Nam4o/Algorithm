from collections import  deque
import sys
input = sys.stdin.readline


A = int(input())

arr = list(map(int, input().split()))

# 거꾸로

ans = deque()
ans.append(-1)
# ans 의 마지막 요소는 항상 -1 (오른쪽 요소 x)

stack = [arr[-1]]
for i in range(2, A + 1):
    if arr[-i] < stack[-1]:
        ans.appendleft(stack[-1])
        stack.append(arr[-i])
    else:
        while stack and arr[-i] >= stack[-1]:
            stack.pop()
        if stack:
            ans.appendleft(stack[-1])
        else:
            ans.appendleft(-1)
        stack.append(arr[-i])
print(*ans)
