import sys
input = sys.stdin.readline
from collections import deque

def solution(number, k):
    answer = ''
    tmp = deque(number)
    stack = []
    cnt = 0
    i = 0
    check = []
    while tmp and cnt < k:
        if not stack:
            stack.append(tmp.popleft())
            check.append(stack[-1])
        # 현재 인덱스의 숫자가 이전에 버
        if tmp[i] > check[-1]:
            while stack and cnt < k:
                if stack[-1] < tmp[i]:
                    stack.pop()
                    cnt += 1
                else:
                    break

            stack.append(tmp.popleft())
            check.append(stack[-1])
        # 현재 인덱스의 숫자가 직전 숫자와 같을경우
        elif tmp[i] == check[-1]:
            check.append(tmp[i])
            stack.append(tmp.popleft())


        else:

            check.append(tmp[i])
            stack.append(tmp[i])
            tmp.popleft()
    
    stack.extend(tmp)
    answer = "".join(stack)
    if cnt != k:
        answer = answer[:len(answer) - (k - cnt)]
    return answer
