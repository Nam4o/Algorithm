N = int(input())

if N % 2 == 1:
    print(int(1 + (4 * (4 ** ((N // 2)) // 3))) % 10007 )
else:
    print(int((3 + (8 * (4 ** ((N // 2 - 1)) // 3))) % 10007))