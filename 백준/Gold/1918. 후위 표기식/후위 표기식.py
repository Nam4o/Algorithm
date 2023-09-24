import sys
input = sys.stdin.readline

arr = input().strip()

stack = []

opers = '()+-/*'

for i in arr:
    if i not in opers:
        print(i, end='')
    elif i == '(':
        stack.append(i)
    elif i in '/*':
        if len(stack) > 0 and stack[-1] in '/*':
            j = stack.pop()
            print(j, end='')
        stack.append(i)
    elif i in '+-':
        while len(stack) != 0 and stack[-1] in '+-/*':
            j = stack.pop()
            print(j, end='')
        stack.append(i)
    elif i == ')':
        while len(stack) != 0 and stack[-1] != '(':
            j = stack.pop()
            print(j, end='')
        stack.pop()

while len(stack) != 0:
    j = stack.pop()
    print(j, end='')

print()