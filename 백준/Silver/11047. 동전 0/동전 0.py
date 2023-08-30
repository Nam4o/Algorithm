N, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

cnt = 0
while K != 0:
    for i in range(1, len(arr) + 1):
        if K // arr[-i] >= 1:
            cnt += K // arr[-i]
            K = K % arr[-i]
print(cnt)