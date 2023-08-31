import sys
input = sys.stdin.readline

N, K = map(int, input().split())

queue = [x for x in range(1, N + 1)]
T = K - 1
print('<', end='')
while queue:
    if len(queue) == 1:
        print(f'{queue.pop()}>')
    else:
        if T <= len(queue) - 1:
            print(queue.pop(T), end=', ')
            T -= 1
        elif T > len(queue) - 1:
            T %= len(queue)
            print(queue.pop(T), end=', ')
            T -= 1
        T += K