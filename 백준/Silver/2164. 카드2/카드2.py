from collections import deque

N = int(input())
queue = deque(list(range(1, N + 1)))

while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    queue.rotate(-1)
