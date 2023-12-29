a, b = input().split()
a = a[::-1]
b = b[::-1]
print(int(str(int(a) + int(b))[::-1]))