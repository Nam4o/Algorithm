tc = int(input())

Yonsei = 0
Korea = 0

for t in range(tc):
    for i in range(0, 9):
        A, B = map(int, input().split())
        Yonsei += A
        Korea += B
    
    if Yonsei > Korea:
        print('Yonsei')
    elif Yonsei < Korea:
        print('Korea')
    else:
        print('Draw')    