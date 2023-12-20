def solution(r1, r2):
    answer = 0
    
    for p in range(1, r2):
        tmp1 = (r2 ** 2 - p ** 2) ** (1 / 2)
        if p < r1:
            tmp2 = (r1 ** 2 - p ** 2) ** (1 / 2)
            if tmp2 == int(tmp2):
                answer += (int(tmp1) - int(tmp2) + 1) * 4
            else:
                answer += (int(tmp1) - int(tmp2)) * 4
        else:
            tmp2 = 0
            answer += (int(tmp1)) * 4
        
    answer += (r2 - r1 + 1) * 4        
    
    return answer

