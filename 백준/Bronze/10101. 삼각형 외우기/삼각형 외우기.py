A = int(input())
B = int(input())
C = int(input())

if A == 60 and B == 60 and C == 60:
    print('Equilateral')
elif A + B + C == 180 and A == B or B == C or A == C:
    print('Isosceles')
elif A + B + C == 180 and A != B and B != C and A != C:
    print('Scalene')
elif A + B + C != 180:
    print('Error')