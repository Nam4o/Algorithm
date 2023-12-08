import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    mx = 0
    ans = ''
    for i in range(n):
        worth, player = input().split()
        if int(worth) > mx:
            mx = int(worth)
            ans = player
    print(ans)

