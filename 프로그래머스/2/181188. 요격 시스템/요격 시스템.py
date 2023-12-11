def solution(targets):
    targets.sort(key=lambda x: (x[0], x[1]))
    answer = 0
    
    main_s, main_e = targets[0]
    cnt = 1
    
    
    for start, end in targets:
        if main_e <= start:
            cnt += 1

            main_s, main_e = start, end
        elif main_s < start and end < main_e:
            
            main_s, main_e = start, end
        
    return cnt