def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices) - 1):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = cnt + 1
                break
            else:
                cnt += 1
            answer[i] = cnt
    return answer