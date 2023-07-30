T = int(input())

for i in range(T):
    R, S = map(str, input().split())

    int_R = int(R)
    blank = ''
    for i in range(len(S)):
        blank += S[i] * int_R
    print(blank)



