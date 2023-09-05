import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def find(A, B, C):
    if B == 1:
        return A % C
    else:
        s = find(A, B // 2, C)
        if B % 2 == 0:
            return s * s % C
        else:
            return s * s * A % C

print(find(A, B, C))