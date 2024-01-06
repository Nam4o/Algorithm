from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

arr = deque(list(map(int, input().split())))

check = 1


stack = []
while True:
    if len(arr) != 0 :
        if arr[0] == check:
            arr.popleft()
            check += 1
        elif len(stack) != 0 and stack[-1] == check:
            stack.pop()
            check += 1
        else:
            stack.append(arr.popleft())
    else:
        while len(stack) != 0 and stack[-1] == check:
            stack.pop()
            check += 1
        if stack:
            print("Sad")
            break
        else:
            print("Nice")
            break


    if arr == [] and stack == []:
        print("Nice")
        break
