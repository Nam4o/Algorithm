def solution(board):
    
    cnt_o = 0
    cnt_x = 0

    check = True
    check_o = False
    check_x = False
    
    for i in range(3):
        
        if board[i].count("X") == 3:
            check_x = True
        if board[i].count("O") == 3:
            check_o = True
        inner_o = 0
        inner_x = 0
        for j in range(3):
            if board[i][j] == "X":
                cnt_x += 1
            elif board[i][j] == "O":
                cnt_o += 1

            if board[j][i] == "X":
                inner_x += 1
            elif board[j][i] == "O":
                inner_o += 1
        if inner_o == 3:
            check_o = True
        if inner_x == 3:
            check_x = True
    inner_o = 0
    inner_x = 0
    for t in range(3):
        
        if board[t][t] == "X":
            inner_x += 1
        elif board[t][t] == "O":
            inner_o += 1
    if inner_o == 3:
        check_o = True
        # if check_o == False:
        #     check_o = True
        # else:
        #     check = False
        #     return 0
    if inner_x == 3:
        check_x = True
        # if check_x == False:
        #     check_x = True
        # else:
        #     check = False
        #     return 0
    inner_o = 0
    inner_x = 0
    for k in range(1, 4):
        
        if board[k - 1][-k] == "X":
            inner_x += 1
        elif board[k - 1][-k] == "O":
            inner_o += 1
    if inner_o == 3:
        check_o = True
        # if check_o == False:
        #     check_o = True
        # else:
        #     check = False
    if inner_x == 3:
        check_x = True
        # if check_x == False:
        #     check_x = True
        # else:
        #     check = False
    if check_o == True:
        if check_x == True or cnt_o <= cnt_x:
            check = False
        else:
            if cnt_o < cnt_x:
                check = False

            if abs(cnt_o - cnt_x) >= 2:
                check = False
    elif check_x == True:
        if cnt_o != cnt_x:
            check = False
        else:
            if cnt_o < cnt_x:
                check = False

            if abs(cnt_o - cnt_x) >= 2:
                check = False
    else:
        if cnt_o < cnt_x:
            check = False

        if abs(cnt_o - cnt_x) >= 2:
            check = False
            
            
    # print(cnt_o, cnt_x)
    if check == False:
        answer = 0
    else:
        answer = 1
    
    return answer

print(solution([".O.","...","..."]))