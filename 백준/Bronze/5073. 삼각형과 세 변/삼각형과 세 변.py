while True:
    A, B, C = map(int, input().split())
    num_list = [A, B, C]
    num_list.sort(reverse=True)
    t = num_list.pop(0)
    if A == 0 and B == 0 and C == 0:
        break
    if t >= sum(num_list):
        print('Invalid')
    elif A == B and B == C and A == C:
        print('Equilateral')
    elif A == B or B == C or A == C:
        print('Isosceles')
    elif A != B and B != C and A != C:
        print('Scalene ')