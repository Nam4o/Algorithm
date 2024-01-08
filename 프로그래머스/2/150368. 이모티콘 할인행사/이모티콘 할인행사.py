from itertools import product

def solution(users, emoticons):
    dc = [10, 20, 30, 40]
    
    tmp = []
    answer = []
    cases = list(product(dc, repeat = len(emoticons)))
    for i in cases:
        cnt = 0
        amount = 0
        for user in users:
            inner_amount = 0
            for j in range(len(emoticons)):
                if i[j] >= user[0]:
                    inner_amount += (100 - i[j]) * emoticons[j] // 100
                if inner_amount >= user[1]:
                    cnt += 1
                    break;
                if j == len(emoticons) - 1:
                    amount += inner_amount
        tmp.append([cnt, amount])           
    # print(tmp)
    tmp.sort(key=lambda x: (-x[0], -x[1]))
    answer.append(tmp[0])
    # print(cases)
    return answer[0]