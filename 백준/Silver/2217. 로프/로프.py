import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

rope = [int(input()) for _ in range(N)]
rope.sort()
rope = deque(rope)

result = []
while len(rope) > 1:
    if len(rope) > 1 and len(rope) * rope[0] > rope[-1]:
        result.append(len(rope) * rope[0])
        rope.popleft()
        # print(len(rope) * rope[0])
        # break
    else:
        if len(rope) == 1:
            result.append(rope[-1])
        else:
            rope.popleft()
if N == 1:
    print(rope[0])
else:
    print(max(result))