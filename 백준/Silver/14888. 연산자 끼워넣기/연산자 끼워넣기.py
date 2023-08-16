N = int(input())

def f(i, N):
    global result
    if i == N:

        x = 0
        while stack_oper != []:
            a = num_arr.pop(0)
            b = num_arr.pop(0)
            if stack_oper[x] == '+':
                num_arr.insert(0, a + b)
            elif stack_oper[x] == '-':
                num_arr.insert(0, a - b)
            elif stack_oper[x] == '*':
                num_arr.insert(0, a * b)
            elif stack_oper[x] == '/':
                if a < 0:
                    num_arr.insert(0, -((-a) // b))
                else:
                    num_arr.insert(0, a // b)
            if len(num_arr) == 1:
                result.append(num_arr.pop())
                for k in arr:
                    num_arr.append(k)
                break
            x += 1

    else:
        for j in range(i, N):    # 자신부터 오른쪽 끝까지
            stack_oper[i], stack_oper[j] = stack_oper[j], stack_oper[i]
            f(i + 1, oper_N)
            stack_oper[i], stack_oper[j] = stack_oper[j], stack_oper[i]

oper_N = N - 1



arr = list(map(int, input().split()))
num_arr = []
for k in arr:
    num_arr.append(k)
oper = list(map(int, input().split()))
stack_oper = []
for t in range(4):
    if t == 0 and oper[t] != 0:
        for r in range(oper[t]):
            stack_oper.append('+')
    elif t == 1 and oper[t] != 0:
        for r in range(oper[t]):
            stack_oper.append('-')
    elif t == 2 and oper[t] != 0:
        for r in range(oper[t]):
            stack_oper.append('*')
    elif t == 3 and oper[t] != 0:
        for r in range(oper[t]):
            stack_oper.append('/')
result = []
if len(stack_oper) >= 2:
    f(0, oper_N)
    print(max(result))
    print(min(result))
elif len(stack_oper) == 1:
    if stack_oper[0] == '+':
        print(arr[0] + arr[1])
        print(arr[0] + arr[1])
    elif stack_oper[0] == '-':
        print(arr[0] - arr[1])
        print(arr[0] - arr[1])
    elif stack_oper[0] == '*':
        print(arr[0] * arr[1])
        print(arr[0] * arr[1])
    elif stack_oper[0] == '/':
        print(arr[0] // arr[1])
        print(arr[0] // arr[1])

