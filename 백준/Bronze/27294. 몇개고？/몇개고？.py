t, s = map(int, input().split())
if s == 1 and t < 12 or t > 16:
    print(280)
elif s == 0 and 12 <= t <= 16:
    print(320)
else:
    print(280)