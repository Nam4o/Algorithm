import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

possible = True

while S != T:
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
    if T == []:
        possible = False
        break

if possible:
    print(1)
else:
    print(0)