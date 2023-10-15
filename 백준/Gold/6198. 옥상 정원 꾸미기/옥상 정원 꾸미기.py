import sys
input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]

stack = [arr[0]]

cnt = 0

for i in range(1, N):
    while stack:
        if arr[i] >= stack[-1]:
            stack.pop()
        else:
            break
            
    stack.append(arr[i])
    cnt += len(stack) - 1
    
print(cnt)
