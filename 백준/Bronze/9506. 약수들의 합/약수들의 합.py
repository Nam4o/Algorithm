import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    stack = []
    i = 1
    while i != n:
        if n % i == 0:
            stack.append(i)
        i += 1
    if sum(stack) == n:
        print(f'{n} = ', end='')
        for j in stack:
            if j != stack[-1]:
                print(f'{j} + ', end='')
            else:
                print(j)
    else:
        print(f'{n} is NOT perfect.')
