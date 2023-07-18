point_1, point_2, point_3 = map(int, input().split())

if point_1 == point_2 == point_3:
    print(10000 + (point_1 * 1000))
elif point_1 == point_2 != point_3:
    print(1000 + (point_1 * 100))
elif point_1 != point_2 == point_3:
    print(1000 + (point_2 * 100))
elif point_1 == point_3 != point_2:
    print(1000 + (point_1 * 100))
else:
    print(max(point_1, point_2, point_3) * 100)
