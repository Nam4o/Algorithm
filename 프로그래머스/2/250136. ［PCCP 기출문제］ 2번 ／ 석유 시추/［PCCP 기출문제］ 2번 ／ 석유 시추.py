from collections import deque

def solution(land):
    row = len(land)
    col = len(land[0])
    tmp = {}
    
    check = [[False for _ in range(col)] for _ in range(row)]
    
    numbering = -1
    def bfs(start): 
        
        cnt = 1
        queue = deque()
        queue.append(start)
        check[start[0]][start[1]] = True
        land[start[0]][start[1]] = numbering
        
        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
        mx = 0
        
        while queue:
            n = queue.popleft()
            for k in range(4):
                ni, nj = n[0] + di[k], n[1] + dj[k]
                if 0 <= ni < row and 0 <= nj < col and check[ni][nj] == False and land[ni][nj] == 1:
                    check[ni][nj] = True
                    cnt += 1
                    queue.append([ni, nj])
                    land[ni][nj] = numbering
                    

        tmp[numbering] = cnt
        

                
                    
    for i in range(row):
        for j in range(col):
            if land[i][j] == 1 and check[i][j] == False:

                check[i][j] = True
                bfs([i, j])
                numbering -= 1
    answer = 0
    
    
    for i in range(col):
        cnt1 = 0
        check1 = False
        tmp_list = []
        for j in range(row):
            
            if land[j][i] != 0 and check1 == False:
                if land[j][i] not in tmp_list:
                    tmp_list.append(land[j][i])
                    cnt1 += tmp[land[j][i]]
                    check1 = True
            elif land[j][i] == 0:
                check1 = False

            if cnt1 > answer:
                answer = cnt1
    return answer