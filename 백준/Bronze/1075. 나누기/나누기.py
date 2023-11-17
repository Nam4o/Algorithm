import sys
input = sys.stdin.readline

N = int(input())
F = int(input())

tmp = str(N)
tmp2 = tmp[:len(tmp) - 2]

isDone = False
while not isDone:
    for j in range(10):
        for i in range(10):
            tmp3 = tmp2 + str(j) + str(i)
            if int(tmp3) % F == 0:
                isDone = True
                print(str(j) + str(i))
                break
        if isDone:
            break

