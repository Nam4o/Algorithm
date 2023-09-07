import sys
input = sys.stdin.readline

arr = list(input().strip())


stack = []
stack.append(arr[0])
num_stack = []
is_ans = True

spc = '()[]'

i = 1
if len(arr) == 1:
    is_ans = False

while len(arr) > 1:
    if i == len(arr):
        is_ans = False
        break
    if stack[-1] == '(' and arr[i] == ']':
        is_ans = False
        break
    elif stack[-1] == '[' and arr[i] == ')':
        is_ans = False
        break
    elif stack[-1] == '(' and arr[i] == ')':
        if arr[i - 1] == '(':
            arr[i - 1] = 2
            arr.pop(i)
            stack.clear()
            stack.append(arr[0])
            i = 1
        elif str(arr[i - 1]) not in spc:
            arr[i - 1] *= 2
            arr.pop(i)
            stack.clear()
            stack.append(arr[0])
            i = 1
        else:
            is_ans = False
            break
    elif stack[-1] == '[' and arr[i] == ']':
        if arr[i - 1] == '[':
            arr[i - 1] = 3
            arr.pop(i)
            stack.clear()
            stack.append(arr[0])
            i = 1
        elif str(arr[i - 1]) not in spc:
            arr[i - 1] *= 3
            stack.clear()
            stack.append(arr[0])
            arr.pop(i)
            i = 1
        else:
            is_ans = False
            break
    elif str(arr[i]) not in spc and str(arr[i - 1]) not in spc:
        arr[i - 1] += arr[i]
        arr.pop(i)
        stack.clear()
        stack.append(arr[0])
        i = 1
    else:
        if str(arr[i]) not in spc:
            if 0< i < len(arr) - 1 and arr[i - 1] == '(' and arr[i + 1] == ')':
                arr[i - 1] = arr[i] * 2
                arr.pop(i)
                arr.pop(i)
                stack.clear()
                stack.append(arr[0])
                i = 1
            elif 0< i < len(arr) - 1 and arr[i - 1] == '[' and arr[i + 1] == ']':
                arr[i - 1] = arr[i] * 3
                arr.pop(i)
                arr.pop(i)
                stack.clear()
                stack.append(arr[0])
                i = 1
            else:
                i += 1
            continue
        else:
            stack.append(arr[i])
            i += 1

if is_ans == True:
    print(* arr)
else:
    print(0)