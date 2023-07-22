A = int(input())
B = str(input())



for i in range(1, len(B) + 1):
    print(f'{A * int(B[-i])}')
print(f'{A * int(B)}')