people = int(input())

agree = 0
disagree = 0
for i in range(people):
    opinion = int(input())
    if opinion == 1:
        agree += 1
    elif opinion == 0:
        disagree += 1


if agree > disagree:
    print('Junhee is cute!')
elif agree < disagree:
    print('Junhee is not cute!')
