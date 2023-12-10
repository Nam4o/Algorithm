answer = 0
length = 0

def solution(numbers, target):
    global answer, length
    answer = 0
    length = len(numbers)
    
    
    
    def recur(depth, current):
        global answer, length
        if depth == length - 1:
            if current == target:
                answer += 1
            return
        
        recur(depth + 1, current + numbers[depth + 1])
        recur(depth + 1, current - numbers[depth + 1])
        
    recur(0, numbers[0])
    recur(0, -numbers[0])
    
    
    return answer
