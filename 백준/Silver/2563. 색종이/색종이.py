paper = int(input())

N = 100

board = [[0]*100 for _ in range(N)]

for i in range(paper):
    start, end = map(int, input().split())

    for k in range(start, start + 10):
        for j in range(end, end + 10):
            board[j][k] = 1

result = 0
for i in range(N):
    result += sum(board[i])

print(result)


