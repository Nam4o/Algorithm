number = int(input())

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0


for i in range(1, number + 1):
    A, B = map(int, input().split())
    if A > 0:
        if B > 0:
            Q1 += 1
        elif B < 0:
            Q4 += 1
        else:
            AXIS += 1
    elif A < 0:
        if B > 0:
            Q2 += 1
        elif B < 0:
            Q3 += 1
        else:
            AXIS += 1
    else:
        AXIS += 1
        
print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')
