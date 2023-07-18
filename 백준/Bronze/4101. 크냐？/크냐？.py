A, B = map(int, input().split())

while True:
    if A > B:
        print('Yes')
        A, B = map(int, input().split())
    elif A + B == 0:
        break        
    elif A <= B:
        print('No')
        A, B = map(int, input().split())
