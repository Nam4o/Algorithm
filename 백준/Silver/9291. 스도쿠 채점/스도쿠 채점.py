T = int(input())
 
for tc in range(1, T + 1):
    try:
        numbers = [list(map(int, input().split())) for _ in range(9)]
    
        count = 0
    
        for i in range(9):
            linear_sum = []
            for j in range(9):
                linear_sum.append(numbers[i][j])
            if sum(linear_sum) != 45:
                count += 1
                break
            else:
                continue
            
            
        for i in range(9):
            vertical_sum = []
            for j in range(9):
                vertical_sum.append(numbers[j][i])
            if sum(vertical_sum) != 45:
                count += 1
                break
            else:
                continue

            
        di = [0, 1, 0, -1, 1, -1, 1, -1, 0]
        dj = [1, 0, -1, 0, 1, -1, -1, 1, 0]
    
    
        find_range = [1, 4, 7]

        for i in find_range:
            for j in find_range:
                s = []
                for k in range(9):
                    ni, nj = i + di[k], j + dj[k]
                    if numbers[ni][nj] in s:
                        break
                    else:
                        s.append(numbers[ni][nj])
                if sum(s) != 45:
                    count += 1
                    break
                else:
                    continue
                
        if count == 0:
            print(f'Case {tc}: CORRECT')
        else:
            print(f'Case {tc}: INCORRECT')


        space = input()
        pass
    except:
        break