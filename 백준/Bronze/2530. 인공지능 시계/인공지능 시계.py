H, M, S = map(int, input().split())
time = int(input())
lap_S = S + (time)

    
if lap_S >= 60:
    M += (lap_S // 60)
    if M >= 60:
        H += (M // 60)
        H %= 24
        M %= 60 

    print(H, M, str(lap_S%60))     
else:
    print(H, M, str(lap_S))