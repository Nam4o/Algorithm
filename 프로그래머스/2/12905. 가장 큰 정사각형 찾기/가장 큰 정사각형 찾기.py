def solution(board):
    length_1 = len(board)
    length_2 = len(board[0])
    
    mx = 0
    
    for i in range(length_1):
        for j in range(length_2):
            if board[i][j] != 0 and mx == 0:
                    mx = 1
            if i != 0 and j != 0 and board[i][j] != 0:
                
                if board[i - 1][j - 1] != 0 and board[i - 1][j] != 0 and board[i][j - 1] != 0:
                    board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                    if board[i][j] > mx:
                        mx = board[i][j]
            
                
    return mx ** 2