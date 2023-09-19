def n_queen_solve(N):
    def check(row, col):
        for i in range(row):
            if abs(i - row) == abs(board[i] - col):
                return False
        return True

    def nqueen(row):
        nonlocal cnt
        if row == N:
            cnt += 1
            return
        for col in range(N):
            if not visited[col] and check(row, col):
                board[row] = col
                visited[col] = True
                nqueen(row + 1)
                visited[col] = False

    cnt = 0
    board = [-1] * N
    visited = [False] * N

    nqueen(0)
    return cnt


N = int(input())
cnt = n_queen_solve(N) 
print(cnt)