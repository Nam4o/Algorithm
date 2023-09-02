import sys
input = sys.stdin.readline

N = int(input())

def find(s, e, n):
    global blue_cnt
    global white_cnt

    tmp = 0

    for i in range(s, s + n):
        for j in range(e, e + n):
            if arr[i][j] == 1:
                tmp += 1
    if tmp == n ** 2:
        blue_cnt += 1
        return
    elif tmp == 0:
        white_cnt += 1
        return
    else:
        mid = n // 2
        find(s, e, mid)
        find(s + mid, e,mid)
        find(s, e + mid, mid)
        find(s + mid, e + mid, mid)


arr = [list(map(int, input().split())) for _ in range(N)]

blue_cnt = 0
white_cnt = 0
find(0,0,N)
print(white_cnt)
print(blue_cnt)