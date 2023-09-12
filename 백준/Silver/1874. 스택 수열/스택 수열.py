import sys
input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]

num = [x for x in range(1, N + 1)]

is_possible = True
stack = []
j = 0
result = []
i = 0
while True:
    if i == N or is_possible == False:
        break
    while stack:
        if arr[i] in stack and arr[i] != stack[-1]:
            is_possible = False
            break
        elif arr[i] == stack[-1]:
            stack.pop()
            j -= 1
            num.pop(j)
            i += 1
            result.append('-')
        else:
            stack.append(num[j])
            j += 1
            result.append('+')
    else:
        if i == N or is_possible == False:
            break
        stack.append(num[j])
        j += 1
        result.append('+')

if is_possible:
    for i in result:
        print(i)
else:
    print('NO')
