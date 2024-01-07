import sys
input = sys.stdin.readline

p, m = map(int, input().split())

room = [[]]

for i in range(p):
    a, id = input().split()
    level = int(a)
    if i == 0:
        room[0].append([level, id])
        continue
    for j in range(len(room)):

        if len(room[j]) < m and room[j][0][0] - 10 <= level <= room[j][0][0] + 10:
            room[j].append([level, id])
            break
        else:
            if j == len(room) - 1:
                room.append([[level, id]])

for r in room:
    if len(r) == m:
        r.sort(key=lambda x: x[1])
        print("Started!")
        for k in range(m):
            print(*r[k])
    else:
        r.sort(key=lambda x: x[1])
        print("Waiting!")
        for k in range(len(r)):
            print(*r[k])

