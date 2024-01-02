def solution(k, d):
    answer = 0
    res = []
    
    for i in range(0, d + 1, k):
        j = (d ** 2 - i ** 2) ** (1 / 2)
        res.append(j // k)
        answer += j // k + 1
        
        
    return answer