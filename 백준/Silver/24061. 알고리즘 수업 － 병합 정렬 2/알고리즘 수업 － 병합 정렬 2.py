import sys
input = sys.stdin.readline

def mergeSort(A, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(A, l, mid)
        mergeSort(A, mid + 1, r)
        merge(A, l, mid, r)


def merge(A, l, mid, r):
    global cnt
    global check
    i, j, t = l, mid + 1, 0

    tmp = [0] * (r - l + 1)
    while i <= mid and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1
    while i <= mid:
        tmp[t] = A[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1
    i, t = l, 0
    while(i <= r):

        A[i] = tmp[t]
        i += 1
        t += 1
        cnt += 1
        if cnt == K:
            check = True
            print(*A)
            break

N, K = map(int, input().split())

A = list(map(int, input().split()))
tmp = A[:]
cnt = 0
check = False
mergeSort(A, 0, N - 1)

if check == False:
    print(-1)
