def solution(cards):
    answer = 0
    stack = []
    
    tmp_card = []
    check = []
    while sum(stack) != len(cards):
        for idx in cards:
            tmp = idx
            if idx not in check:
                tmp_card.append(idx)
                check.append(idx)
                print(idx)
                while True: 
                    if cards[tmp - 1] in check:
                        stack.append(len(tmp_card))
                        tmp_card = []
                        break
                    else:
                        check.append(cards[tmp - 1])
                        tmp_card.append(cards[tmp - 1])
                        tmp = cards[tmp - 1]

                    # tmp_card.append(cards[idx - 1])
                    # check.append(cards[idx - 1])
            
            # if tmp_card != []:
            #     stack.append(len(tmp_card))

    if len(stack) == 1:
        answer = 0
    elif len(stack) == 2:
        answer = stack[0] * stack[1]
    else:
        stack.sort()
        answer = stack[-1] * stack[-2]
    return answer


    