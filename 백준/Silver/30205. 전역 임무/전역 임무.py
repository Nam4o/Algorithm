import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())


possible = True
for j in range(N):
    if possible:
        tmp = sorted(list(map(int, input().split())))
    else:
        tmp = list(map(int, input().split()))
    stack = []
    if possible:
        for i in tmp:
            if i == -1:
                stack.append(True)
            else:
                if P >= i:
                    P += i
                else:
                    if stack:
                        nxt = False
                        for t in range(len(stack)):
                            stack.pop()
                            P *= 2
                            if P >= i:
                                P += i
                                nxt = True
                                break
                        if not nxt:
                            possible = False

                    else:
                        possible = False
        while stack:
            stack.pop()
            P *= 2

if possible:
    print(1)
else:
    print(0)

