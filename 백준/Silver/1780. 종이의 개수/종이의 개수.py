import sys
input = sys.stdin.readline


def recur(s, e, n):
    global ans_1, ans_2, ans_3
    if N == 1:
        if arr[s][e] == -1:
            ans_1 += 1
            return
        elif arr[s][e] == 0:
            ans_2 += 1
            return
        elif arr[s][e] == 1:
            ans_3 += 1
            return

    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0

    for i in range(s, s + n):
        for j in range(e, e + n):
            if cnt_2 == 0 and cnt_3 == 0 and arr[i][j] == -1:
                cnt_1 += 1
            elif cnt_1 == 0 and cnt_3 == 0 and arr[i][j] == 0:
                cnt_2 += 1
            elif cnt_1 == 0 and cnt_2 == 0 and arr[i][j] == 1:
                cnt_3 += 1
            else:
                break

    if cnt_1 == n ** 2:
        ans_1 += 1
        return
    elif cnt_2 == n ** 2:
        ans_2 += 1
        return
    elif cnt_3 == n ** 2:
        ans_3 += 1
        return
    else:
        mid = n // 3
        recur(s, e, mid)
        recur(s + mid, e, mid)
        recur(s + 2 * mid, e, mid)
        recur(s, e + mid, mid)
        recur(s, e + 2 * mid, mid)
        recur(s + mid, e + mid, mid)
        recur(s + mid, e + 2 * mid, mid)
        recur(s + 2 * mid, e + mid, mid)
        recur(s + 2 * mid, e + 2 * mid, mid)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


ans_1 = 0
ans_2 = 0
ans_3 = 0
recur(0, 0, N)

print(ans_1)
print(ans_2)
print(ans_3)
