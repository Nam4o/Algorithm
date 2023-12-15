def solution(plans):
    answer = []
    for i in plans:
        i[1] = (int(i[1][:2]) * 60 + int(i[1][3:5]))
        i[2] = int(i[2])
        print(i[2])
    stack = []
    
    
    plans.sort(key=lambda x: x[1])
    now_time = plans[0][1]
    # print(f'현재 시각 : {now_time}')
    
    
    for j in range(1, len(plans)):
#         # 이전 과제 완료 예상 시간
        previous = now_time + plans[j - 1][2]
        # print(previous)
#         # 현재 작업이 시작 시간의 시각이 이전 작업 종료 시간의 시각과 같거나 작을 경우
        
        if plans[j][1] < previous:
            now_time = plans[j][1]
            stack.append([plans[j - 1][0], previous - now_time])
        elif plans[j][1] > previous:
            answer.append(plans[j - 1][0])
            while previous <= plans[j][1]:
                if stack:
                    if previous + stack[-1][1] <= plans[j][1]:
                        now_time = previous + stack[-1][1]
                        previous = now_time
                        answer.append(stack.pop()[0])
                    else:
                        now_time = plans[j][1]
                        stack[-1][1] -= now_time - previous
                        break
                else:
                    now_time = plans[j][1]
                    break
            if not stack:
                now_time = plans[j][1]
        else:
            answer.append(plans[j - 1][0])
            now_time = plans[j][1]
                    
        if j == len(plans) - 1:
            answer.append(plans[j][0])
    while stack:
        answer.append(stack.pop()[0])

    
    return answer

# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# korean english math
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# science history computer music
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
# bbb ccc aaa
# print(solution([["science", "12:40", "80"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# science history computer music
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "20"], ["ccc", "12:20", "20"],["ddd","12:30","20"],["eee","12:50","20"],["fff","13:30","100"],["ggg","14:00","100"],["hhh","14:30","100"],["ttt","15:00","100"]]))
# d e c b t h g f a
# print(solution( [["a", "09:00", "10"], ["b", "09:10", "10"], ["c", "09:15", "10"], ["d", "09:30", "10"], ["e", "09:35", "10"]]))
# a c b e d
print(solution( [["a", "09:00", "30"], ["b", "09:20", "10"], ["c", "09:40", "10"]]))
# b a c
# print(solution([["A", "11:50", "30"], ["B", "13:00", "20"], ["C", "13:10", "30"]]))
#  A C B

