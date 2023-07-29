import math

tc = int(input())

for i in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance < r1 + r2 and abs(r1-r2) < distance:
        print(2)
    elif distance == r1 + r2 or abs(r1-r2) == distance and distance != 0:
        print(1)
    elif distance > r1 + r2 or distance < abs(r1 - r2):
        print(0)
    elif distance == 0 and r1 == r2:
        print(-1) 