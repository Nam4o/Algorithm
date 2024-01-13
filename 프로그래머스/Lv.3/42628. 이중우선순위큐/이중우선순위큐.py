import heapq, sys
input = sys.stdin.readline

def solution(operations):
    answer = []
    
    low = []
    high = []
    
    for o in operations:
        tmp = o.split(" ")
        tmp[1] = int(tmp[1])

        if tmp[0] == "I":
            if tmp[1] < 0:
                heapq.heappush(low, tmp[1])
            else:
                heapq.heappush(high, -tmp[1])
        else:
            if tmp[1] == 1:
                if high:
                    heapq.heappop(high)
                else:
                    if low:
                        low.remove(max(low))
            else:
                if low:
                    heapq.heappop(low)
                else:
                    if high:
                        high.remove(max(high))
                    

    if high:
        answer.append(-heapq.heappop(high))
        if low:
            answer.append(heapq.heappop(low))
        elif high:
            answer.append(-max(high))
        else:
            answer.append(answer[0])
    elif low:
        tmp_pop = heapq.heappop(low)
        if low:
            answer.append(max(low))
            answer.append(tmp_pop)
        else:
            answer.append(tmp_pop)
            answer.append(tmp_pop)
    else:
        answer = [0, 0]
            
            
        
    return answer