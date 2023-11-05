from collections import deque
import sys
input = sys.stdin.readline


def rotation(num, way):
    num1 = num // 1000
    num2 = (num % 1000) // 100
    num3 = (num % 100) // 10
    num4 = num % 10

    if way == 1:
        return num2 * 1000 + num3 * 100 + num4 * 10 + num1
    else:
        return num4 * 1000 + num1 * 100 + num2 * 10 + num3

def bfs(A, B):
    queue = deque()
    queue.append([A,''])
    dp[A] = True

    while queue:
        n, cmd = queue.popleft()

        if dp[(n * 2) % 10000] == False:
            if (n * 2) % 10000 == B:
                print(cmd + 'D')
                break
            queue.append([((n * 2) % 10000), cmd + 'D'])
            dp[(n * 2) % 10000] = True
        if n == 0:
            if dp[9999] == False:
                if 9999 == B:
                    print(cmd + 'S')
                    break
                queue.append([9999, cmd + 'S'])
        elif n > 0:
            if dp[n - 1] == False:
                if n - 1 == B:
                    print(cmd + 'S')
                    break
                queue.append([n - 1, cmd + 'S'])
                dp[n - 1] = True
        if dp[rotation(n, 1)] == False:
            if rotation(n, 1) == B:
                print(cmd + 'L')
                break
            queue.append([rotation(n, 1), cmd + 'L'])
            dp[rotation(n, 1)] = True
        if dp[rotation(n, -1)] == False:
            if rotation(n, -1) == B:
                print(cmd + 'R')
                break
            queue.append([rotation(n, -1), cmd + 'R'])
            dp[rotation(n, -1)] = True


T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    dp = [False] * 10001
    bfs(A, B)

