N = int(input())

agree = 0
disagree = 0


for i in range(N):
    A = int(input())
    if A == 1:
        agree += 1
    else:
        disagree += 1

if agree > disagree:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')