import sys
input = sys.stdin.readline

n, game = input().split()
n = int(n)

players = set()
for i in range(n):
    player = input()
    players.add(player)

many = len(players)

if game == 'Y':
    print(many)
elif game == 'F':
    print(many // 2)
else:
    print(many // 3)
