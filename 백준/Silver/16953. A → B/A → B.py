A, B = map(int, input().split())

def cut(B):
    B = B // 2
    return B

def popOne(B):
    B = str(B)
    B = B[:-1]
    if B == '':
        return
    else:
        return int(B)

cnt = 1

while True:
    if B == A:
        print(cnt)
        break
    if B == None:
        print(-1)
        break
    if B % 2 == 0:
        B = cut(B)
    elif str(B)[-1] == '1':
        if B == '':
            print(-1)
            break
        B = popOne(B)
    else:
        print(-1)
        break
    cnt += 1