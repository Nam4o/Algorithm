N, new_record, P = map(int, input().split())

if N > 0:
    scores = list(map(int, input().split()))
    for i in range(len(scores)):
        if len(scores) < P:
            if new_record >= scores[i]:
                print(i + 1)
                break
            elif new_record < scores[-1]:
                print(N + 1)
                break
 
        elif len(scores) >= P:
            if new_record <= scores[P - 1]:
                print(-1)
                break
            elif new_record >= scores[i]:
                print(i + 1)
                break
else:
    print(1)