import sys
input = sys.stdin.readline

stack = list(input().strip())
top = len(stack)
N = int(input())

extra = []

for _ in range(N):
    command = list(input().split())
    if command[0] == 'L':
        if stack:
            extra.append(stack.pop())
    if command[0] == 'D':
        if extra:
            stack.append(extra.pop())
    if command[0] == 'B':
        if stack:
            stack.pop()
    if command[0] == 'P':
        stack.append(command[1])
while extra:
    stack.append(extra.pop())

print(''.join(stack))