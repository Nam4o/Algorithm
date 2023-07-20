cube = int(input())

A, B, C, D, E, F = map(int, input().split())

special = [(A + B + C + D + E), (A + B + C + D + F), (A + B + C + E + F), (A + B + D + E + F),
           (A + C + D + E + F), (B + C + D + E + F),]

if cube == 1:
    print(min(special))
else:
    two = ((4*(cube-1)) + (4)*(cube-2))
    three = 4
    one = (4 * (cube-1) * (cube - 2)) + ((cube-2)**2)




    top = [(A + B + C), (A + B + D), (A + E + C), (A + E + D),
       (B + C + F), (B + D + F),
       (C + E + F),
       (D + E + F)]

    bottom = [(A + B), (A + C), (A + D), (A + E),
          (B + C), (B + D), (B + F), 
          (C + E), (C + F), 
          (D + E), (D + F),
          (E + F)]

    mid = [A, B, C, D, E, F]

    print(min(top)*three + min(bottom)*two + min(mid)*one)
