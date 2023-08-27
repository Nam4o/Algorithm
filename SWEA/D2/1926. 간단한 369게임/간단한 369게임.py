N = int(input())

for i in range(1, N + 1):
    a = str(i)
    cnt = 0
    if '3' in a or '6' in a or '9' in a:
        cnt += a.count('3')
        cnt += a.count('6')
        cnt += a.count('9')
        a = '-' * cnt
    if i == N:
        print(a)
    else:
        print(a, end=' ')