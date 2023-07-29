N = int(input())
star = ''
for i in range(N):
    star += '*'
    print(' '*(N-i-1) + star)