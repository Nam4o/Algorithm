import sys
input = sys.stdin.readline

arr = input().strip()
bomb = list(input().strip())

stack = []


a = len(bomb)

t = 0
while t < len(arr):
    for i in arr:
        if len(stack) >= a and stack[-a:] == bomb:
            for j in range(a):
                stack.pop()

            stack.append(i)
        else:
            stack.append(i)
        t += 1
    if len(stack) >= a and stack[-a:] == bomb:
        for j in range(a):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
