from collections import deque
import sys
input = sys.stdin.readline

def superbfs(c1, c2):

    queue1 = deque()
    queue2 = deque()

    visited1[c1[0]][c1[1]] = 1
    visited2[c2[0]][c2[1]] = 1

    queue1.append(c1)
    queue2.append(c2)

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue1 and queue2:
        n1 = queue1.popleft()
        n2 = queue2.popleft()
        if n1[2] > 10 or n2[2] > 10:
            continue

        for k in range(4):
            ni1, nj1 = n1[0] + di[k], n1[1] + dj[k]
            ni2, nj2 = n2[0] + di[k], n2[1] + dj[k]
            if 0 <= ni1 < N and 0 <= nj1 < M and 0 <= ni2 < N and 0 <= nj2 < M :

                if arr[ni1][nj1] != '#' and arr[ni2][nj2] != '#':
                    queue1.append([ni1, nj1, n1[2] + 1])
                    queue2.append([ni2, nj2, n2[2] + 1])

                elif arr[ni1][nj1] == '#' and arr[ni2][nj2] != '#':
                    queue1.append([n1[0], n1[1], n1[2] + 1])
                    queue2.append([ni2, nj2, n2[2] + 1])

                elif arr[ni2][nj2] == '#' and arr[ni1][nj1] != '#' :
                    queue1.append([ni1, nj1, n1[2] + 1])
                    queue2.append([n2[0], n2[1], n2[2] + 1])


            elif (ni1 < 0 or ni1 >= N or nj1 < 0 or nj1 >= M) and 0 <= ni2 < N and 0 <= nj2 < M:
                if n1[2] > 10 or n2[2] > 10:
                    return print(-1)
                else:

                    return print(n1[2])

            elif (ni2 < 0 or ni2 >= N or nj2 < 0 or nj2 >= M) and 0 <= ni1 < N and 0 <= nj1 < M:
                if n1[2] > 10 or n2[2] > 10:
                    return print(-1)
                else:

                    return print(n1[2])

    return print(-1)


N, M = map(int, input().split())


arr = [list(input().strip()) for _ in range(N)]


coin_1 = []
coin_2 = []

visited1 = [[0] * M for _ in range(N)]
visited2 = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'o':
            if not coin_1:
                coin_1 = [i, j, 1]
            else:
                coin_2 = [i, j, 1]

superbfs(coin_1, coin_2)